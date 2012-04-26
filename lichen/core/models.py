from django.db import models


class Map(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class Wall(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.ForeignKey(Map)
