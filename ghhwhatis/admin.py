from ghhwhatis.models import DifferncePage
from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin


class DifferncePageAdmin(DisplayableAdmin):

    fieldsets = [
        ("Title",                       {'fields': ['title']}),
        ("Published Date",              {'fields': ['publish_date']}),
        ("Published Status",            {'fields': ['status']}),
        ("Subject One",                 {'fields': ['subject_one']}),
        ("Subject Two",                 {'fields': ['subject_two']}),
        ("Subject One Data",            {'fields': ['subject_one_data']}),
        ("Subject Two Data",            {'fields': ['subject_two_data']}),
    ]

    list_display = ('title', 'status', 'publish_date', 'subject_one', 'subject_two',)
    list_editable = ('status',)
    list_filter = ['status', 'publish_date',]
    search_fields = ['title',]
    date_hierarchy = 'publish_date'

admin.site.register(DifferncePage, DifferncePageAdmin)

