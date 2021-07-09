from django.db import models
#from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields, widgets
from django.forms.widgets import EmailInput
from .models import UserProfile, TeleModel, Category




class CreateUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User 

        fields = ['email', 'password1', 'password2']


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(username__iexact=email).exists():
            raise forms.ValidationError('A user has already registered using this email')
        return email

    
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)

        user.email = self.cleaned_data['email']
        user.username = user.email


        if commit:
            user.save()
        return user
    



class ModelUploadForm(forms.ModelForm):

    categories = Category.objects.all()

    
    title = forms.CharField(min_length=5,  max_length=255, label=("Title"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title', 'id':'title'}))
    description = forms.CharField(min_length=5 ,label=("Description"), widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Some description', 'id':'descriptionfield', 'rows': '5'}))
    category = forms.ModelChoiceField(label=('Category'), queryset=categories, widget=forms.Select(attrs={'class': 'form-control', 'id':'category'}))
    #category = forms.ChoiceField(choices=choice_list, label=("Category"), widget=forms.Select(attrs={'class': 'form-control'}))
    version = forms.FloatField(label=("Version"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Version', 'id':'version'}))
    require_version = forms.FloatField(label=("Requires Telegram version"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telegram version', 'id':'require_version'}))
    logo = forms.ImageField(widget=forms.FileInput(attrs={'id': 'logo-input', 'onchange': "readURL(this)"}))
    file = forms.FileField(widget=forms.FileInput(attrs={'id': 'file-input'}))
    
    class Meta:
        model = TeleModel
        fields = ('title', 'description', 'category', 'version', 'require_version', 'logo', 'file')


    # def clean_version(self):
    #     version = self.cleaned_data.get('version')
    #     require_version = self.cleaned_data.get('require_version')

    #     if 


    #     if User.objects.filter(username__iexact=email).exists():
    #         raise forms.ValidationError('A user has already registered using this email')
    #     return email


class UserForm(forms.ModelForm):

    first_name = forms.CharField(min_length=2,  max_length=255, label=("Name"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name', 'aria-describedby': 'nameHelp', 'id':'namefield'}))
    email = forms.EmailField(min_length=2,  max_length=255, label=("Email"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your email(to contact)', 'aria-describedby': 'emailHelp', 'id':'emailfield'}))

    class Meta:
        model = User
        fields = ('first_name','email')

class UserProfileForm(forms.ModelForm):

    website = forms.CharField(min_length=2,  max_length=255, label=("Website"), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your website', 'aria-describedby': 'siteHelp', 'id':'sitefield'}))

    avatar = forms.ImageField(widget=forms.FileInput(attrs={'id': 'file-input', 'onchange': "readURL(this)"}))
    
    class Meta:
        model = UserProfile
        fields = ('website', 'avatar')

