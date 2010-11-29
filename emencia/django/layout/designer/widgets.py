#!/usr/bin/env python
# -*- coding: utf-8 -*-


# django import
from django import forms

from django.conf import settings

from django.core.urlresolvers import reverse
from django.core.exceptions import ImproperlyConfigured

from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode


class LayoutDesignerWidget(forms.Textarea):
    """
    """

    class Media:
        try:
            js = (
                settings.LAYOUT_DESIGNER_MEDIA_PREFIX + 'bewype-yui3-gallery/yui/yui.js',
                settings.LAYOUT_DESIGNER_MEDIA_PREFIX + 'layout-designer/js/layout.designer.js'
            )

            css = { 'all': (settings.LAYOUT_DESIGNER_MEDIA_PREFIX
                + 'layout-designer/css/layout.designer.css',) }
        except AttributeError:
            raise ImproperlyConfigured("django-emencia-layout-designer"\
                    " requires LAYOUT_DESIGNER_MEDIA_PREFIX setting. This"\
                    " setting specifies a URL prefix to the ckeditor JS and"\
                    " CSS media (not uploaded media). Make sure to use a"\
                    " trailing slash:"\
                    " LAYOUT_DESIGNER_MEDIA_PREFIX = '/media/ckeditor/'")

    def render(self, name, value, attrs={}):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        return mark_safe(u'''<div id='%s' class='yui3-skin-sam'>%s</div><br/>
<center><a id="designer_preview" href="#">Preview</a></center><br/>
<input id="content_id" "type="hidden" value="%s" name="content_id"/>
<input id="upload_url" "type="hidden" value="%s" name="content_id"/>
<input id="file_static_path" "type="hidden" value="%s" name="content_id"/>''' % (
    final_attrs['id'], force_unicode(value),
    final_attrs['id'], reverse('layout_designer_upload'),
    settings.LAYOUT_DESIGNER_MEDIA_PREFIX + 'uploads/'))

