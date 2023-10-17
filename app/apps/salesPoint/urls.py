from django.urls import path
from . import views

urlpatterns = [
    path('', views.SalesPointListView.as_view(), name='salesPointList'),
    path('list', views.SalesPointListZoneView, name='salesPointListZone'),
    path('create', views.SalesPointCreate, name='salesPointCreate'),
    path('<slug:slug>', views.SalesPointDetailView.as_view(), name='salesPointView'),
    path('ro/<slug:slug>', views.SalesPointDetailViewZone.as_view(), name='salesPointViewZone'),
    path('edit/<slug:slug>', views.SalesPointUpdate.as_view(), name='salesPointEdit'),
    path('delete/<slug:slug>', views.SalesPointDelete.as_view(), name='salesPointDelete'),
    path('report/<int:sales_point_id>', views.download_sale_point_report, name='download_sale_point_report'),

]