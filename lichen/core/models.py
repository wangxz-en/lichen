from django.db import models


class Map(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


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


class Lichen(Point):
    '''Roaming energy source

    For now, all lichens are spherical
    '''

    diameter = models.IntegerField(default=3)
