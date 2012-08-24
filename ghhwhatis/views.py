from ghhwhatis.models import DifferncePage
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
#from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect

def what_is(request, page_slug):
    diffdata = get_object_or_404(DifferncePage, slug=page_slug)
    return render_to_response('ghhwhatis/index.html',
                       {'diffdata':diffdata},
                        context_instance=RequestContext(request))

def explore_a_z(request, page_slug):
    explore_alphebet_section = DifferncePage.objects.filter(slug__startswith=page_slug)
    return render_to_response('pages/explore-topics-list.html',
                       {'explore_alphebet_section':explore_alphebet_section, 'page_slug':page_slug},
                        context_instance=RequestContext(request))

def home(request):
    most_recent = DifferncePage.objects.filter(status=2).order_by('-publish_date')[:10]
    return render_to_response('index.html',
                       {'most_recent':most_recent},
                        context_instance=RequestContext(request))



