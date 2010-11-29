#!/usr/bin/env python
# -*- coding: utf-8 -*-

# django import
from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^upload/', 'emencia.django.layout.designer.views.upload', name='layout_designer_upload')
)

