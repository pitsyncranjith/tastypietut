from django.conf.urls import patterns, include, url
from .api import DemoResource

demo_resource = DemoResource()

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tastypietut.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^api/', include(demo_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
