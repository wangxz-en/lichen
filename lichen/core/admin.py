from lichen.core.models import Map, Cell, Wall, Unit
from django.contrib import admin

for m in [Map, Cell, Wall, Unit]:
    admin.site.register(m)