from django.db import models
from mezzanine.core.models import Displayable, RichTextField


class DifferncePage(Displayable):
    subject_one = models.CharField(max_length=400, verbose_name="First Subject", blank=True)
    subject_two = models.CharField(max_length=400, verbose_name="Second Subject", blank=True)
    subject_one_data = RichTextField(blank=True, verbose_name="Subject One Data")
    subject_two_data = RichTextField(blank=True, verbose_name="Subject Two Data")

    @models.permalink
    def get_absolute_url(self):
        return ('ghhwhatis.views.what_is', [self.slug,])

    def __unicode__(self):
        return self.title

