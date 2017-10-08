# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import csv
from django.http import HttpResponse
from .models import Position


def download(request):
    # Create the HttpResponse object with the appropriate CSV header.
    response = HttpResponse() #content_type='text/csv')
    # response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
    writer = csv.writer(response)
    writer.writerow(['timestamp', 'x', 'y', 'z'])
    for obj in Position.objects.all()[:100]:
        writer.writerow(map(str, [obj.timestamp, obj.x, obj.y, oby.z]))
    return response
