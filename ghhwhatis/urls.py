from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic import TemplateView
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('ghh.ghhwhatis.views',
    url("^$", "compare", name="compare"),
    url(r'^(?P<page_slug>[\w-]+)/$', 'what_is'),
    url(r'^flippa_5439457.txt', TemplateView.as_view(
        template_name='generic/flippa.html')),
)



