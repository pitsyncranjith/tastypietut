from tastypie.resources import ModelResource
from tastypie.constants import ALL
from simpleapp.models import Demo


class DemoResource(ModelResource):
	class Meta:
		queryset = Demo.objects.all()
		resource_name = 'demo'
		filtering = {"name" : ALL}
		
