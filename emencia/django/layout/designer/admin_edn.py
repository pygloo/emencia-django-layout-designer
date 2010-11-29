"""ModelAdmin for Newsletter
"""

# django import
from django import forms
from django.contrib import admin

# edn import
from emencia.django.newsletter.models import Newsletter
from emencia.django.newsletter.admin import NewsletterAdmin

# layout designer import
from emencia.django.layout.designer.widgets import LayoutDesignerWidget

# unregister
admin.site.unregister(Newsletter)

class NewsletterLayoutDesignerForm(forms.ModelForm):

    content = forms.CharField(widget=LayoutDesignerWidget())

    class Meta:
        model = Newsletter

class  NewsletterLayoutDesignerAdmin(NewsletterAdmin):
    form = NewsletterLayoutDesignerForm
    inlines = ()

# re-register
admin.site.register(Newsletter, NewsletterLayoutDesignerAdmin)

