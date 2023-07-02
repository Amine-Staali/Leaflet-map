from django.urls import path
from . import views
urlpatterns = [
    path('add_node/', views.Locate, name='add_node'),
    path('add_poly/', views.add_poly, name='add_poly'),
]
