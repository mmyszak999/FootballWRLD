from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'FW'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('create-player/', views.createplayer, name='create_player'),
    path('create-club/', views.createclub, name="create_club"),
    path('club/<int:pk>', views.ClubView.as_view(), name="club"),
    path('draft/', views.draft, name='draft'),
    path('filter-player/', views.FilterView.as_view(), name='filter_player'),
    path('player/<int:pk>', views.PlayerView.as_view(), name="player"),
    path('players-database/', views.PlayersDatabaseView.as_view(), name='players_database'),
    path('clubs-database/', views.ClubsDatabaseView.as_view(), name='clubs_database'),
    path('random-player/', views.get_random_player, name='random_player'),
    path('draft-results/', views.draft_results, name='draft_results'),

]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
