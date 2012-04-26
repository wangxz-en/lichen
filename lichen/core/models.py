from django.db import models


class Map(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class Cell(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.ForeignKey(Map)


class Wall(Cell):
    pass


class Unit(Cell):
    type = models.CharField(max_length=30)
