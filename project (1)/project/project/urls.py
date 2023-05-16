"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path
from app_1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('movies/', views.get_all_movies, name='movies'),
    path('directors/', views.get_all_directors, name='alldirectors'),
    path('details/<int:id>', views.get_director_details, name='directordetails'),
    path('add_director/', views.add_director, name='addirector'),
    path('add_movie/', views.add_movie, name='addMovie'),
    path('editdirector/<int:id>', views.edit_director, name='editdirector'),
    path('deletedirectorconfirmation/<int:id>', views.delete_director_confirmation, name='confirmdeletion'),
    path('deletedirector/<int:id>', views.delete_director, name='delete'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),

]
