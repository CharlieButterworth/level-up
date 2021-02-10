
from django.db import models


class Game(models.Model):

    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    gametype = models.ForeignKey("GameType", on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    title = models.CharField(max_length=75)
    maker = models.CharField(max_length=75)
    number_of_players = models.IntegerField()
    skill_level = models.IntegerField()
