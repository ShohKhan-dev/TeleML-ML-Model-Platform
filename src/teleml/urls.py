from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.contrib.auth import views

from .views import *
from .api import *


urlpatterns = [
    path("", home, name='home'),
    path('register/', register, name='register'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login'),
    path('u/<int:pk>/', userprofile, name='userprofile'),


    #path('profile/update/',  UpdateProfile.as_view(), name='update_profile'),
    path('upload/', upload_model, name='upload_model'),

    path('model/edit/<int:pk>/', model_edit, name='model_edit'),

    path('model/<int:pk>/', model_description, name='model_description'),

    path('model/delete/<int:pk>/', model_delete, name='model_delete'),

    path('category/<int:pk>/', category_item, name='category_item'),

    path('search/', search_results, name='search')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


