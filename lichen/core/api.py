from tastypie.resources import ModelResource

from models import Map


class MapResource(ModelResource):
    class Meta:
        queryset = Map.objects.all()
        resource_name = 'map'