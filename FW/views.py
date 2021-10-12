from django.shortcuts import render, redirect
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

    def get_queryset(self):
        return Club.objects.all()


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


def id_list(max_number):
    x = []
    counter = 0
    for p in range(1, max_number + 1):
        x.append(p)
        counter += 1
    return x


def random_five_players(pl_list):
    random_list = []
    counter = 0
    while counter != 5:
        random_id = random.choice(pl_list)
        if random_id in random_list:
            continue
        else:
            random_list.append(random_id)
            counter += 1
    return random_list


def delete_ids(main_list, list_to_delete):
    for number in range(0, 5):
        main_list.remove(list_to_delete[number]["id"])
    return main_list


def draft(request):
    id_amount = Player.objects.count()
    list_id = id_list(id_amount)
    all_players = Player.objects.all()

    all_gk = all_players.filter(position="GK").values("id", "name", "surname")
    random_gk = random_five_players(all_gk)
    delete_ids(list_id, random_gk)

    all_def = all_players.filter(position="DEF").values("id", "name", "surname")
    random_def = random_five_players(all_def)
    delete_ids(list_id, random_def)

    all_mid = all_players.filter(position="MID").values("id", "name", "surname")
    random_mid = random_five_players(all_mid)
    delete_ids(list_id, random_mid)

    all_att = all_players.filter(position="ATT").values("id", "name", "surname")
    random_att = random_five_players(all_att)
    delete_ids(list_id, random_att)

    last_slot_players = all_players.filter(id__in=list_id).values("id", "name", "surname").exclude(position="GK")
    random_last_slot_players = random_five_players(last_slot_players)
    delete_ids(list_id, random_last_slot_players)

    test = all_players.filter(id__in=list_id)

    context = {
        "random_gk": random_gk,
        "random_def": random_def,
        "random_mid": random_mid,
        "random_att": random_att,
        "random_last_slot_players": random_last_slot_players,
        "list_id": list_id,
        "test": test,
    }

    return render(request, "FW/Draft.html", context)