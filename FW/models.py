from django.db import models
from django.urls import reverse



class Club(models.Model):
    club_name = models.CharField(max_length=100)
    foundation_date = models.IntegerField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.club_name


class Player(models.Model):
    name = models.CharField(max_length=60)
    surname = models.CharField(max_length=70, blank=True)
    nationality = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    club = models.ForeignKey(Club, on_delete=models.CASCADE)
    position = models.CharField(choices=(
        ('GK', 'Goalkeeper'),
        ('DEF', 'Defender'),
        ('MID', 'Midfielder'),
        ('ATT', 'Attacker'),
    ), max_length=21)
    height = models.PositiveIntegerField(default=0)
    weight = models.PositiveIntegerField(default=0)
    foot = models.CharField(choices=(
        ('L', 'Left'),
        ('R', 'Right')
    ), max_length=10, default="Right")

    def __str__(self):
        return self.name + " " + self.surname

    def get_absolute_url(self):
        return reverse("player", kwargs={'pk': self.pk})