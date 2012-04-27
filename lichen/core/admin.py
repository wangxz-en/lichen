from lichen.core.models import *
from django.contrib import admin

for m in [Map, Cell, Wall, Unit, Lichen, LichenTile]:
    admin.site.register(m)
