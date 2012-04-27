import random
from functools import partial

from django.db import models


class Map(models.Model):
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)


class Point(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.ForeignKey(Map)

    class Meta:
        abstract = True


class Cell(Point):
    class Meta:
        unique_together = ('x', 'y', 'map')


class Wall(Cell):
    destructible = models.BooleanField(default=False)


class Unit(Cell):
    type = models.CharField(max_length=30)

    def move(self, x, y):
        pass


def random_speed():
    random.triangular(-1, 1)


class Lichen(models.Model):
    '''Roaming energy source
    '''

    x_speed = models.FloatField(default=partial(random.choice, [1, -1]))
    y_speed = models.FloatField(default=random_speed)
    z_speed = models.FloatField(default=random_speed)

    max_tiles = models.IntegerField(default=5)


class LichenTile(Point):
    lichen = models.ForeignKey(Lichen)

    class Meta:
        unique_together = ('x', 'y', 'map')
