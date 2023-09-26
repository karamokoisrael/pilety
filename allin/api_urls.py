from django.urls import path
from . import api_views as views

api_routes = [
    path('api/', views.recent_cargos),
    path('api/', views.cargos_list),
    path('api/', views.containers_list),
    path('api/', views.unloaded_cargo),
    path('api/', views.generate_invoice),
]