from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views import generic

from .forms import *
from .filters import PlayerFilter

import random


class IndexView(generic.ListView):
    template_name = 'FW/index.html'

    def get_queryset(self):
        return True


class CreatePlayerView(generic.ListView):
    template_name = 'FW/CreatePlayer.html'

    def get_queryset(self):
        return True


class FilterView(generic.ListView):
    model = Player
    template_name = 'FW/FilterPlayer.html'

    def get_queryset(self):
        return Player.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = PlayerFilter(self.request.GET, queryset=self.get_queryset())
        return context


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
        form = CreateClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/FootballWRLD/')

    context = {"form": form}
    return render(request, "FW/CreateClub.html", context)


def get_random_player(request):
    random_player = random.choice(Player.objects.all())
    player = Player.objects.get(id=random_player.id)
    return render(request, "FW/Player.html", {"player": player})


def draft(request):
    players_gk = list(Player.objects.filter(position="GK"))
    random_gk = random.sample(players_gk, 5)
    players_def = list(Player.objects.filter(position="DEF"))
    random_def = random.sample(players_def, 5)
    players_mid = list(Player.objects.filter(position="MID"))
    random_mid = random.sample(players_mid, 5)
    players_att = list(Player.objects.filter(position="ATT"))
    random_att = random.sample(players_att, 5)
    player_last_slot = list(Player.objects.exclude(position="GK"))
    random_last_slot = random.sample(player_last_slot, 5)
    context = {
        "random_gk": random_gk,
        "random_def": random_def,
        "random_mid": random_mid,
        "random_att": random_att,
        "random_last_slot": random_last_slot,
    }
    return render(request, "FW/Draft.html", context)