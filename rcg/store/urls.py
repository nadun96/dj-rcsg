from django.urls import path
from . import views

urlpatterns = [
    path('manage', views.manage , name='manage'),
    path('items', views.items , name='items'),
    path('broken', views.broken , name='broken_items'),
    path('lend', views.lend , name='lend_items'),
    path('reports', views.reports , name='Stock_reports'),
]
