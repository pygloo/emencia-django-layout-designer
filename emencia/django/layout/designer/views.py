#!/usr/bin/env python
# -*- coding: utf-8 -*-

# python import
import os, json

# django import
from django.conf import settings
from django.http import HttpResponse

try:
    from django.views.decorators.csrf import csrf_exempt
except ImportError:
    # monkey patch this with a dummy decorator which just returns the same function
    # (for compatability with pre-1.1 Djangos)
    def csrf_exempt(fn):
        return fn

# bewype import
from emencia.django.layout.designer import utils

def _get_file_info( file_ ):
    # prepare data
    file_.seek(0)
    _data = file_.read()
    # get file (img) info
    _type, _width, _height = utils.get_image_info(_data)
    # return info
    return {
            'contentType': _type,
            'imgHeight': _height,
            'imgWidth' : _width
            }

@csrf_exempt
def upload(request):
    """
    """
    # get file object from request
    _file = request.FILES['file']
    # get unique file name
    _file_name = utils.random_str(24)
    # get uploads path
    _uploads_path = settings.EDLD_UPLOADS
    if os.path.exists( _uploads_path ):
        # do save
        _file_out = open(os.path.join(_uploads_path, _file_name), 'wb+')
        # Iterate through chunks and write to destination.
        for _chunk in _file.chunks():
            _file_out.write(_chunk)
        # get some info about this file
        _file_info = _get_file_info(_file_out)
        _file_out.close()
        # ..
        _file_info['fileName'] = _file_name
        # return generated file name
        return HttpResponse(json.dumps(_file_info))
    else:
        return HttpResponse('')

