from django.urls import path
from . import views

urlpatterns = [
    path('', views.FormListView.as_view(), name='formList'),
    path('create', views.FormCreate, name='formCreate'),
    path('<slug:slug>', views.FormDetailView.as_view(), name='formView'),
    path('edit/<slug:slug>', views.FormUpdate.as_view(), name='formEdit'),
    path('delete/<slug:slug>', views.FormDelete.as_view(), name='formDelete'),

]