#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django import
from django.db import models
from django import forms

# emencia import
from emencia.django.layout.designer.widgets import LayoutDesignerWidget

class LayoutDesignerFormField(forms.fields.Field):

    widget = LayoutDesignerWidget

    def __init__(self, *args, **kwargs):
        kwargs.update({'widget': LayoutDesignerWidget})
        super(LayoutDesignerFormField, self).__init__(*args, **kwargs)

class LayoutDesignerField(models.TextField):

    def formfield(self, **kwargs):
        defaults = {
            'form_class': LayoutDesignerFormField,
            'widget': LayoutDesignerWidget,
        }
        defaults.update(kwargs)
        return super(LayoutDesignerField, self).formfield(**defaults)

