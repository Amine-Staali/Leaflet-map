from django.contrib import admin
from django.contrib.gis.admin import GISModelAdmin
from .models import *
# Register your models here.

class NodeAdmin(GISModelAdmin):
    list_display = ['location']

admin.site.register(Node, NodeAdmin)

class PolyAdmin(GISModelAdmin):
    list_display = ['location']

admin.site.register(Poly, PolyAdmin)