from django.shortcuts import render, redirect
from .models import Projekcija, Karta
from django.contrib.auth import get_user_model
from .forms import KartaForm
from django.http import HttpResponseNotAllowed

# Ovdje idu controlleri

def home(request):
    greeting = "Hello"
    return render(request, "home.html", {"data": greeting})

def main(request):
    return render(request, "main.html")

def getAllMovies(request):
    movies = Projekcija.objects.all()
    return render(request, "movies.html", {"data": movies})

def getFilmById(request, id):
    movie = Projekcija.objects.get(pk=id)
    return render(request, "movie.html", {"data": movie})

def getAllUsers(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, "users.html", {"data": users})

def getAllTickets(request):
    tickets = Karta.objects.all()
    return render(request, "tickets.html", {"data": tickets})

def buyTicket(request):
    if request.method == "GET":
        form = KartaForm()
        return render(request, "buyTicket.html", {"form": form})
    elif request.method == "POST":
        form = KartaForm(request.POST)
        film = Projekcija.objects.all()
        if form.is_valid():

            form.save()
            return redirect('tickets')
    else:
        return HttpResponseNotAllowed()