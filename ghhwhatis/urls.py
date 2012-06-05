from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

from mezzanine.core.views import direct_to_template

urlpatterns = patterns('ghhwhatis.views',
#    url(r'^(?P<pageslug>\w+)/$', 'what_is'),
    url(r'^test/$', 'what_is'),

)



