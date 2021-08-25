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


class DraftView(generic.ListView):
    template_name = 'FW/Draft.html'

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
        print("Printing POST: ", request.POST)
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
