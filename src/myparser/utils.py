import csv
import os
from django.conf import settings

from .models import ParsedData


def handle_uploaded_file(f):
    """Function saves uploaded file to /media/, then reads data from the file.
    After parsing, data becomes a python dictionary - it makes easy to save data
    in database. Then we make a queryset to prepare data for google charts.

    """
    with open(os.path.join(settings.MEDIA_ROOT, 'test.csv'), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

    file = open(os.path.join(settings.MEDIA_ROOT, 'test.csv'), 'r')
    reader = csv.DictReader(file)

    for row in reader:
        region = row['Область']
        city = row['Город']
        value = row['Значение']
        my_obj, created = ParsedData.objects.get_or_create(region=region, city=city, value=value)
        if created:
            my_obj.save()

    queryset = ParsedData.objects.values('region').distinct()
    return queryset


def handle_queryset(queryset):
    """Function takes a queryset as an argument and returns sorted data,
    ready for converting into json - AmChart will receive a multiple dataset
    and we can use menu to choose any Region we need.

    """
    result = []
    for q in queryset:
        filter_param = q['region']
        each_region_data = ParsedData.objects.filter(region__iexact=filter_param).order_by('-value')
        pre_result = []

        for each in each_region_data:
            info = dict(region=each.region, city=each.city, value=each.value)
            pre_result.append(info)
        result.append(pre_result)
    return result
