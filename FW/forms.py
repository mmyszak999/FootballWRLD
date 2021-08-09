from django.forms import ModelForm
from .models import Player, Club


class CreatePlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = '__all__'


class CreateClubForm(ModelForm):
    class Meta:
        model = Club
        fields = '__all__'