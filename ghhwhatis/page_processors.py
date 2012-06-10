from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from ghhwhatis.models import DifferncePage
#from django.utils.translation import ugettext_lazy as _
from ghhwhatis.data_apis import *
from mezzanine.utils.urls import slugify

@processor_for('explore-topics')
def get_atoz(request, page):
    alphabet_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    alpha_dict = {}
    diffpages = DifferncePage.objects.all().order_by('slug')
    for l in alphabet_list:
        alpha_dict[l] =  [dp.slug for dp in diffpages if dp.slug[0] == l]

    return{'alpha_dict':alpha_dict,}



class DifferenceForm(forms.Form):
    subject_one = forms.CharField(initial='Subject One')
    subject_two = forms.CharField(initial='Subject Two')

@processor_for('compare')
def get_data(request, page):
    form = DifferenceForm(auto_id='%s')

    if request.method == "POST":
        form = DifferenceForm(request.POST, auto_id='%s')
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
                print 'obj does not exist'
                
                try:
                    subject_one_subject=get_subject_one_data(word_list_sorted[0])['query']
                    subject_one_description = get_subject_one_data(word_list_sorted[0])['description']
                    subject_one_description_dictservice ='<p />'.join(get_subject_one_data_dictservice(word_list_sorted[0])['data'])
                except Exception:
                    errormsg1 = "Not Found. Check spelling. Make singular. Could be tech glitch!"
                    return{'form':form,'errormsg1':errormsg1}

                try:
                    subject_two_subject=get_subject_two_data(word_list_sorted[1])['query']
                    subject_two_description = get_subject_two_data(word_list_sorted[1])['description']
                    subject_two_description_dictservice ='<p />'.join(get_subject_two_data_dictservice(word_list_sorted[1])['data'])
                except Exception:
                    errormsg2 = "Not Found. Check spelling. Make singular. Could be tech glitch!"
                    return{'form':form,'errormsg2':errormsg2}

                subject_data_sources_api ='<ul>{0} {1}</ul>'.format(
                    '<li />'.join(get_subject_one_data_dictservice(word_list_sorted[0])['sources']),
                    '<li />'.join(get_subject_two_data_dictservice(word_list_sorted[1])['sources']),
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

    return{'form':form,}
