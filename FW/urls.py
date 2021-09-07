from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'FW'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('CreatePlayer/', views.createplayer, name='CreatePlayer'),
    path('CreateClub/', views.createclub, name="CreateClub"),
    path('Club/<int:pk>', views.ClubView.as_view(), name="Club"),
    path('Draft/', views.DraftView.as_view(), name='Draft'),
    path('FilterPlayer/', views.FilterView.as_view(), name='FilterPlayer'),
    path('Player/<int:pk>', views.PlayerView.as_view(), name="Player"),
    path('PlayersDatabase/', views.PlayersDatabaseView.as_view(), name='PlayersDatabase'),
    path('ClubsDatabase/', views.ClubsDatabaseView.as_view(), name='ClubsDatabase'),
]
# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
