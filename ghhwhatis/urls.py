from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('ghh.ghhwhatis.views',
    url("^$", "compare", name="compare"),
    url(r'^(?P<page_slug>[\w-]+)/$', 'what_is'),
)



