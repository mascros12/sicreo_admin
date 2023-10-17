from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('create', views.DivisionCreate, name='divisionCreate'),
    path('', views.DivisionListView.as_view(), name='divisionList'),
    path('<slug:slug>', views.DivisionDetailView.as_view(), name='divisionDetail'),
    #path('edit/<slug:slug>', views.DivisionUpdate.as_view(), name='divisionEdit'),
    path('edit/<int:division_id>', views.DivisionUpdate, name='divisionEdit'),
    path('delete/<slug:slug>', views.DivisionDelete.as_view(), name='divisionDelete'),

]
