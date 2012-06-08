from django import forms
from django.http import HttpResponseRedirect
from mezzanine.pages.page_processors import processor_for
from ghhwhatis.models import DifferncePage
#from django.utils.translation import ugettext_lazy as _
from ghhwhatis.data_apis import *
from mezzanine.utils.urls import slugify

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
                except Exception:
                    errormsg1 = "First Subject Not Found. Could be a technical glitch or spelling error."
                    return{'form':form,'errormsg1':errormsg1}

                try:
                    subject_two_subject=get_subject_two_data(word_list_sorted[1])['query']
                    subject_two_description = get_subject_two_data(word_list_sorted[1])['description']
                except Exception:
                    errormsg2 = "Second Subject Not Found. Could be a technical glitch or spelling error."
                    return{'form':form,'errormsg2':errormsg2}

                obj = DifferncePage(title=page_title, subject_one=subject_one_subject, subject_two=subject_two_subject,
                                    subject_one_data=subject_one_description,
                                   subject_two_data=subject_two_description, )
                obj.save()

                redirect = "{0}{1}/".format(request.path, page_slug)
                return HttpResponseRedirect(redirect)

    return{'form':form,}
