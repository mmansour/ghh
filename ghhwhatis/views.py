from ghhwhatis.models import DifferncePage
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect

def what_is(request):
    
    return render_to_response('ghhwhatis/index.html',
                       {},
                        context_instance=RequestContext(request))

