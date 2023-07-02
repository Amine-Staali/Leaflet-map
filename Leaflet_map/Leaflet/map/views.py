from django.shortcuts import render
from .models import *
import json
from django.contrib.gis.geos import Point,Polygon


def Locate(request):
    if request.method == 'POST':
        lat = float(request.POST.get('lat'))
        lng = float(request.POST.get('long'))
        point = Point(lng, lat)
        instance = Node()
        instance.location = point
        instance.save()
    return render(request, 'map/add_node.html', {})

def add_poly(request):
    if request.method == 'POST':
        polygon_coordinates = request.POST.get('polygon_coordinates')
        coordinates = json.loads(polygon_coordinates)
        polygon = Polygon(coordinates)
        
        instance = Poly()
        instance.location = polygon
        instance.save()
        
    return render(request, 'map/add_poly.html',{})