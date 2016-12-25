from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .models import Line, Location


def locations(request):
	locations = serialize('geojson', Location.objects.all(),
		geometry_field='point',
		fields=('name', 'address', 'city', 'state',)
	)
	return JsonResponse(locations, safe=False)

def lines(request):
	lines = serialize('geojson', Line.objects.all(),
		geometry_field='line',
		fields=('name', 'description')
	)
	return JsonResponse(lines, safe=False)
