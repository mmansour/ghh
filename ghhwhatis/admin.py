from ghhwhatis.models import DifferncePage
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin


class DifferncePageAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",                       {'fields': ['title']}),
        ("Title Casing?",            {'fields': ['is_title_case']}),
        ("Published Date",              {'fields': ['publish_date']}),
        ("Published Status",            {'fields': ['status']}),
        ("Allow Comments",            {'fields': ['allow_comments']}),
        ("Subject One",                 {'fields': ['subject_one']}),
        ("Subject Two",                 {'fields': ['subject_two']}),
        ("Summary",                 {'fields': ['summary']}),

        ("Subject One Data",            {'fields': ['subject_one_data']}),
        ("Subject Two Data",            {'fields': ['subject_two_data']}),

        ("Subject One Video",            {'fields': ['subject_one_video']}),
        ("Subject Two Video",            {'fields': ['subject_two_video']}),

        ("Subject One Image",            {'fields': ['subject_one_image']}),
        ("Subject Two Image",            {'fields': ['subject_two_image']}),

        ("Subject One Ad",            {'fields': ['subject_one_ad']}),
        ("Subject Two Ad",            {'fields': ['subject_two_ad']}),

        ("Subject One Data Dict Service",            {'fields': ['subject_one_data_dictservice']}),
        ("Subject Two Data Dict Service",            {'fields': ['subject_two_data_dictservice']}),
        ("Data Sources",            {'fields': ['subject_data_sources']}),
    ]

    list_display = ('title', 'status', 'publish_date', 'subject_one', 'subject_two', 'allow_comments',)
    list_editable = ('status', 'allow_comments')
    list_filter = ['status', 'publish_date',]
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(DifferncePage, DifferncePageAdmin)

