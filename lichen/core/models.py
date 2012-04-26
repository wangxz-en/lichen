from django.db import models


class Map(models.Model):
    width = models.IntegerField()
    height = models.IntegerField()


class Cell(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    map = models.ForeignKey(Map)

    class Meta:
        unique_together = ('x', 'y', 'map')


class Wall(Cell):
    destructible = models.BooleanField(default=False)


class Unit(Cell):
    type = models.CharField(max_length=30)
