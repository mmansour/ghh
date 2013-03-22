from django.db import models
from django.db.models import Q
from mezzanine.core.models import Displayable, RichTextField
from mezzanine.generic.fields import CommentsField, RatingField
from django.utils.translation import ugettext_lazy as _


class DifferncePage(Displayable):

    subject_one = models.CharField(max_length=400, verbose_name="First Subject", blank=True)
    subject_two = models.CharField(max_length=400, verbose_name="Second Subject", blank=True)

    summary = models.TextField(blank=True, verbose_name="Summary of the Diff")

    subject_one_data = models.TextField(blank=True, verbose_name="Subject One Data")
    subject_two_data = models.TextField(blank=True, verbose_name="Subject Two Data")

    subject_one_video = models.TextField(blank=True, verbose_name="Subject One Video")
    subject_two_video = models.TextField(blank=True, verbose_name="Subject Two Video")

    subject_one_ad = models.TextField(blank=True, verbose_name="Subject One Ad")
    subject_two_ad = models.TextField(blank=True, verbose_name="Subject Two Ad")

    subject_one_data_dictservice = models.TextField(blank=True, verbose_name="Subject One Data DictService")
    subject_two_data_dictservice = models.TextField(blank=True, verbose_name="Subject Two Data DictService")
    
    subject_data_sources = models.TextField(blank=True, verbose_name="Data Sources")
    
    allow_comments = models.BooleanField(default=True)
    is_title_case = models.BooleanField(default=True)
    comments = CommentsField(verbose_name=_("Comments"))
    rating = RatingField(verbose_name=_("Rating"))

    @models.permalink
    def get_absolute_url(self):
        return ('ghh.ghhwhatis.views.what_is', [self.slug,])

    def get_related_content(self):
        related_data = DifferncePage.objects.filter(
            Q(subject_one__iexact=self.subject_one) | Q(subject_two__iexact=self.subject_one)
            | Q(subject_two__iexact=self.subject_two) | Q(subject_one__iexact=self.subject_two)
        )[:10]
        return related_data

    def __unicode__(self):
        return self.title

