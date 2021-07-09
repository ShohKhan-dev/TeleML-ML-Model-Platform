from typing import ContextManager
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ModelUploadForm, UserProfileForm, UserForm
from django.contrib.auth.models import User
from .models import UserProfile, TeleModel, Category
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):

    return render(request, 'home.html')


def register(request):

    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
            # return redirect('profile', username = user.username)
    else:
        form = CreateUserForm()

    context = {'form': form}

    return render(request, 'register.html', context)


@login_required
def userprofile(request, pk):

    user = get_object_or_404(User, id=pk)
    models = user.models.all()

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES, instance=user)
        userprofile_form = UserProfileForm(request.POST, request.FILES, instance=user.profile)

        if user_form.is_valid() and userprofile_form.is_valid():
            cur_user = user_form.save()
            userprofile_form.save()

            return redirect('userprofile', pk=cur_user.id)
            
        else:
            for error in user_form.errors.values():
                print(error)
            for error in userprofile_form.errors.values():
                print(error)
    else:
        user_form = UserForm(instance=user)
        userprofile_form = UserProfileForm(instance=user.profile)

    

    context = {'user_form': user_form, 'userprofile_form': userprofile_form, 'user': user, 'models': models}

    return render(request, 'userprofile.html', context)



@login_required
def upload_model(request):

    if request.method == "POST":
        form = ModelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            model = form.save(commit=False)
            model.created_by = request.user
            model.save()

            return redirect('model_description', pk=model.id)
        else:
            for error in form.errors.values():
                print(error)
    else:
        form = ModelUploadForm()

    context = {'form': form}

    return render(request, 'upload_model.html', context)

@login_required
def model_edit(request, pk):

    model_ed = get_object_or_404(TeleModel, id=pk)

    if request.method == "POST":
        form = ModelUploadForm(request.POST, request.FILES, instance=model_ed)
        if form.is_valid():
            model = form.save(commit=False)
            model.created_by = request.user
            model.save()

            return redirect('model_description', pk=model.id)
        else:
            for error in form.errors.values():
                print(error)
    else:
        form = ModelUploadForm(instance=model_ed)

    context = {'form': form, 'model': model_ed}

    return render(request, 'edit_model.html', context)


def model_description(request, pk):

    model = get_object_or_404(TeleModel, id=pk)

    context = {'model': model}

    return render(request, 'ml_description.html', context)


def category_item(request, pk):

    category = get_object_or_404(Category, id=pk)

    models = TeleModel.objects.filter(category=category).all()

    paginator = Paginator(models, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #return render(request, 'list.html', {'page_obj': page_obj})

    context = {'category': category, 'page_obj': page_obj}

    return render(request, 'category_item.html', context)



def search_results(request):
    if request.is_ajax():
        game = request.POST.get('game')

        results = TeleModel.objects.filter(title__icontains=game)

        if len(results) > 0 and len(game) > 0:
            data = []
            for result in results:
                item = {
                    'pk': result.id,
                    'title': result.title,
                    'logo': str(result.logo.url)
                }
                data.append(item)
            res = data
        else:
            res = "No results found ..."
        return JsonResponse({'data': res})

    return JsonResponse({})