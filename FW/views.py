from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .forms import *

import random


class IndexView(generic.ListView):
    template_name = 'FW/index.html'

    def get_queryset(self):
        return True


class CreatePlayerView(generic.ListView):
    template_name = 'FW/CreatePlayer.html'

    def get_queryset(self):
        return True


def createplayer(request):
    form = CreatePlayerForm()
    if request.method == 'POST':
        print("Printing POST: ", request.POST)
        form = CreatePlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/FootballWRLD/')

    context = {'form': form}
    return render(request, 'FW/CreatePlayer.html', context)


def createclub(request):
    form = CreateClubForm()
    if request.method == 'POST':
        print("Printing POST: ", request.POST)
        form = CreateClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/FootballWRLD/')

    context = {"form": form}
    return render(request, "FW/CreateClub.html", context)


class DraftView(generic.ListView):
    template_name = 'FW/Draft.html'

    def get_queryset(self):
        return True


class FilterView(generic.ListView):
    template_name = 'FW/FilterPlayer.html'

    def get_queryset(self):
        return True


class PlayerView(generic.DetailView):
    model = Player
    template_name = 'FW/Player.html'


class ClubView(generic.DetailView):
    model = Club
    template_name = 'FW/Club.html'


class PlayersDatabaseView(generic.ListView):
    model = Player
    template_name = 'FW/PlayersDatabase.html'

    def get_queryset(self):
        return Player.objects.all()


class ClubsDatabaseView(generic.ListView):
    model = Club
    template_name = 'FW/ClubsDatabase.html'

    def get_queryset(self):
        return Club.objects.all()


def draw_a_player(request):
    players_ = Player.objects.all()
    random_player = random.choice(players_)["id"]
    return get_object_or_404(Player, pk=random_player)