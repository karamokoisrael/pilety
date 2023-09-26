from django.urls import path
from . import api_views as views

api_routes = [

    path('api/generate_invoice/<int:invoice_number>/', views.GenerateInvoiceView.as_view(), name='generate-invoice'),
    path('api/recent_cargos/', views.RecentCargosView.as_view(), name='recent-cargos'),
    path('api/unloaded_cargo/', views.UnloadedCargoView.as_view(), name='unloaded-cargo'),
    path('api/cargos_list/', views.CargosListView.as_view(), name='cargos-list'),
    path('api/containers_list/', views.ContainersListView.as_view(), name='containers-list'),
    
    # path('api/recent_cargos', views.recent_cargos),
    # path('api/cargos_list', views.cargos_list),
    # path('api/containers_list', views.containers_list),
    # path('api/unloaded_cargo', views.unloaded_cargo),
    # path('api/generate_invoice', views.generate_invoice),
]