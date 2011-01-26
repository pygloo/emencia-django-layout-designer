#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django import
from django import forms

from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode

from emencia.django.layout.designer.settings import MEDIA_URL


class LayoutDesignerWidget(forms.Textarea):
    """
    """

    class Media:
        js = (
            MEDIA_URL + 'js/bewype-yui3-gallery/yui/yui.js',
            MEDIA_URL + 'js/layout.designer.js'
        )

        css = { 'all': (MEDIA_URL + 'css/layout.designer.css',) }

    def render(self, name, value, attrs={}):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'''<div id='%s' class='yui3-skin-sam'>%s</div><br/>
<center><a id="designer_preview" href="#">Preview</a></center><br/>
<input id="content_id" type="hidden" value="%s" name="content_id"/>
<input id="upload_url" type="hidden" value="%s" name="content_id"/>
<input id="file_static_path" type="hidden" value="%s" name="content_id"/>''' % (
    final_attrs['id'], force_unicode(value),
    final_attrs['id'], reverse('layout_designer_upload'),
    MEDIA_URL + 'uploads/'))

