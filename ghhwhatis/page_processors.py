from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from ghhwhatis.models import DifferncePage, Displayable
from django.utils.translation import ugettext_lazy as _
from ghhwhatis.data_apis import *

class DifferenceForm(forms.Form):
    subject_one = forms.CharField(initial='Subject One')
    subject_two = forms.CharField(initial='Subject Two')

@processor_for('compare')
def get_data(request, page):
    form = DifferenceForm(auto_id='%s')

    if request.method == "POST":
        form = DifferenceForm(request.POST, auto_id='%s')
        if form.is_valid():

            sub_one_word = form.cleaned_data['subject_one']
            sub_two_word = form.cleaned_data['subject_two']

            try:
                subject_one_subject=get_subject_one_data(sub_one_word)['query']
                subject_one_description = get_subject_one_data(sub_one_word)['description']
            except Exception:
                errormsg1 = "First Subject Not Found. Could be a technical glitch or spelling error."
                return{'form':form,'errormsg1':errormsg1}

            try:
                subject_two_subject=get_subject_two_data(sub_two_word)['query']
                subject_two_description = get_subject_two_data(sub_two_word)['description']
            except Exception:
                errormsg2 = "Second Subject Not Found. Could be a technical glitch or spelling error."
                return{'form':form,'errormsg2':errormsg2}
            
            page_slug = "{0}-and-{1}".format(subject_one_subject,subject_two_subject)

            obj, created = DifferncePage.objects.get_or_create(title=page_slug, subject_one=sub_one_word, subject_two=sub_two_word,
                                                       subject_one_data=subject_one_description,
                                                       subject_two_data=subject_two_description, defaults={})

            redirect = "{0}{1}".format(request.path, page_slug)
            return HttpResponseRedirect(redirect)
        
    return{'form':form,}

#    sub_one_word = 'spinach'
#    sub_two_word = 'kale'
#
#    subject_one_subject=get_subject_one_data(sub_one_word)['query']
#    subject_two_subject=get_subject_two_data(sub_two_word)['query']
#
#    subject_one_description = get_subject_one_data(sub_one_word)['description']
#    subject_two_description = get_subject_two_data(sub_two_word)['description']
#
#    page_slug = "{0}-and-{1}".format(subject_one_subject,subject_two_subject)
#
#    obj, created = DifferncePage.objects.get_or_create(title=page_slug, subject_one=sub_one_word, subject_two=sub_two_word,
#                                                       subject_one_data=subject_one_description,
#                                                       subject_two_data=subject_two_description,
#                  defaults={})
#
#    return {'subject_one_subject':subject_one_subject,
#            'subject_one_description':subject_one_description,
#            'subject_two_subject':subject_two_subject,
#            'subject_two_description':subject_two_description,
#    }