from django.urls import path
from . import views

urlpatterns = [
    path('', views.ZoneListView.as_view(), name='zoneList'),
    path('create', views.ZoneCreate, name='zoneCreate'),
    path('<slug:slug>', views.ZoneDetailView.as_view(), name='zoneView'),
    path('edit/<slug:slug>', views.ZoneUpdate.as_view(), name='zoneEdit'),
    path('delete/<slug:slug>', views.ZoneDelete.as_view(), name='zoneDelete'),

]