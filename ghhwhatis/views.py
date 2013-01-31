from ghhwhatis.models import DifferncePage
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django import forms
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect

from mezzanine.utils.urls import slugify
from ghhwhatis.data_apis import *
from captcha.fields import CaptchaField
from django.utils.translation import ugettext_lazy as _


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


class DifferenceForm(forms.Form):
    subject_one = forms.CharField(initial='Apple')
    subject_two = forms.CharField(initial='Orange')
    captcha = CaptchaField()


def compare(request):
    form = DifferenceForm(auto_id=True)
    if request.method == "POST":
        form = DifferenceForm(request.POST, auto_id=True)
        if form.is_valid():

            sub_one_word = form.cleaned_data['subject_one'].lower()
            sub_two_word = form.cleaned_data['subject_two'].lower()

            sub_one_word_slugged = slugify(sub_one_word)
            sub_two_word_slugged = slugify(sub_two_word)

            # FORCE WORDS TO BE IN CERTAIN ORDER TO AVOID DUPE CONTENT
            word_list = [sub_one_word_slugged, sub_two_word_slugged]
            word_list_sorted = sorted(word_list)

            page_slug = "{0}-and-{1}".format(word_list_sorted[0],word_list_sorted[1])
            page_title = "{0} and {1}".format(word_list_sorted[0], word_list_sorted[1])

            try:
                obj = DifferncePage.objects.get(subject_one=word_list_sorted[0],subject_two=word_list_sorted[1])
                redirect = "{0}{1}/".format(request.path, obj.slug)
                return HttpResponseRedirect(redirect)

            except DifferncePage.DoesNotExist:
#                print 'This Comparison Does Not Exist. Create It'

                try:
                    subject_one_subject=get_subject_one_data(word_list_sorted[0])['query']
                    subject_one_description = get_subject_one_data(word_list_sorted[0])['description']
                    subject_one_description_dictservice =''.join(get_subject_one_data_dictservice(word_list_sorted[0])['data'])
                except Exception:
                    errormsg1 = "<strong>Error occured (Subject One)</strong>: <ul><li>Tech glitch!</li></ul>"
#                    return{'form':form,'errormsg1':errormsg1}
                    return render_to_response('pages/compare.html',
                       {'form':form,'errormsg1':errormsg1},
                        context_instance=RequestContext(request))

                try:
                    subject_two_subject=get_subject_two_data(word_list_sorted[1])['query']
                    subject_two_description = get_subject_two_data(word_list_sorted[1])['description']
                    subject_two_description_dictservice =''.join(get_subject_two_data_dictservice(word_list_sorted[1])['data'])
                except Exception:
                    errormsg2 = "<strong>Error occured (Subject Two)</strong>: <ul><li>Tech glitch!</li></ul>"
#                    return{'form':form,'errormsg2':errormsg2}
                    return render_to_response('pages/compare.html',
                       {'form':form,'errormsg2':errormsg2},
                        context_instance=RequestContext(request))

                subject_data_sources_api ='{0} {1}'.format(
                    ''.join(get_subject_one_data_dictservice(word_list_sorted[0])['sources']),
                    ''.join(get_subject_two_data_dictservice(word_list_sorted[1])['sources']),
                )

                obj = DifferncePage(title=page_title, subject_one=subject_one_subject, subject_two=subject_two_subject,
                                    subject_one_data=subject_one_description,
                                   subject_two_data=subject_two_description,
                                   subject_one_data_dictservice=subject_one_description_dictservice,
                                   subject_two_data_dictservice=subject_two_description_dictservice,
                                   subject_data_sources = subject_data_sources_api)
                obj.save()

                redirect = "{0}{1}/".format(request.path, page_slug)
                return HttpResponseRedirect(redirect)
    return render_to_response('pages/compare.html',
                       {'form':form},
                        context_instance=RequestContext(request))



