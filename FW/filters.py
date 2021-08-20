import django_filters

from .models import Player


class PlayerFilter(django_filters.FilterSet):

    class Meta:
        model = Player
        fields = {
            'name': ['exact', 'icontains'],
            'surname': ['exact', 'icontains'],
            'nationality': ['exact'],
            'year_of_birth': ['exact', 'lt', 'gt'],
            'club': ['exact'],
            'position': ['exact'],
            'height': ['exact', 'lt', 'gt'],
            'weight': ['exact', 'lt', 'gt'],
            'foot': ['exact']
        }

