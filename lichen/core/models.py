import random
from functools import partial

from django.db import models


class Map(models.Model):
    width = models.IntegerField(default=100)
    height = models.IntegerField(default=100)


class Faction(models.Model):
    map = models.ForeignKey(Map)


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
    faction = models.ForeignKey(Faction)

    class InvalidMove(Exception):
        pass

    def move(self, x, y):
        if 0 < self.x < self.map.width and 0 < self.y < self.map.height and \
           Cell.objects.filter(map=self.map, x=x, y=y).count() == 0:

            self.x = x
            self.y = y

            self.save()

        else:
            raise self.InvalidMove()


random_speed = partial(random.triangular, -1, 1)


class Lichen(models.Model):
    '''Roaming energy source

    Lichens move in 2d on the map according to x and y speeds and
    in a third dimension by increasing or decreasing their footprint
    on the map according to z speed.
    '''

    x_speed = models.FloatField(default=random_speed)
    y_speed = models.FloatField(default=random_speed)
    z_speed = models.FloatField(default=partial(random.choice, [-0.05, -0.05]))

    max_tiles = models.IntegerField(default=5)


class LichenTile(Point):
    lichen = models.ForeignKey(Lichen)

    class Meta:
        unique_together = ('x', 'y', 'map')
