from django.shortcuts import render, redirect
from .models import Director, Movie
from .forms import DirectorForm, MovieForm
from django.http import HttpResponse, HttpResponseNotAllowed
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def home(request):
    nesto = "Hello!"
    return render(request, 'home.html', {"data":nesto})

def get_all_movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies.html', {"data":movies})

def get_all_directors(request):
    movies = Director.objects.all()
    return render(request, 'directors.html', {"data":movies})

def get_director_details(request, id):
    director = Director.objects.get(pk=id)
    print(director)
    return render(request, 'details.html', {"data":director})

def get_director_movies(request):
    director = Director.objects.get(pk=1)
    director_movies = director.filmovi.all()
    print(director_movies)
    return render(request, 'details.html', {"data":director})

def add_director(request):
    if request.method == 'GET':
        form = DirectorForm()
        return render(request, 'add_director.html',{"form": form})
    elif request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addirector')
    else:
        return HttpResponseNotAllowed()


def add_movie(request):
    if request.method == 'GET':
        form = MovieForm()
        return render(request, 'add_movie.html', {"form": form})
    elif request.method == 'POST':
        form = MovieForm(request.POST)
        #print(form.cleaned_data)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect('movies')
        else:
            return HttpResponseNotAllowed()
    else:
            return HttpResponseNotAllowed()

def edit_director(request, id):
    director = Director.objects.get(pk=id)
    if request.method == 'GET':
        form = DirectorForm(instance=director)
        return render(request, 'edit_director.html', {"form":form})
    elif request.method == 'POST':
        form = DirectorForm(request.POST, instance=director)
        if form.is_valid():
            form.save()
            return redirect('alldirectors')
        else:
            return HttpResponseNotAllowed()

def delete_director_confirmation(request, id):
    if request.method == 'GET':
        return render(request, 'confirm_deletion.html', {"data":id})
    else:
        return HttpResponseNotAllowed()

def delete_director(request, id):
    director = Director.objects.get(pk=id)
    if 'da' in request.POST:
        director.delete()
        return HttpResponse('Deleted successfully!')
    else:
        return redirect('alldirectors')

def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'register.html', {"form":form})
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return redirect('register')









        
    




    












