from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('apps.users.urls')), 
    path('', views.index, name='index'),
    path('report/general', views.download_general_report, name='download_general_report'),
    path('report/zone', views.download_zone_report, name='download_zone_report'),
    #API
    path('api/forms', views.apiForms, name='apiForms'),
    path('api/formsQuestions/', views.apiQuestions, name='apiFormsQuestions'),
    path('api/getCompany/', views.apiGetCompany, name='apiGetCompany'),
    path('api/getContact/', views.apiGetContact, name='apiGetContact'),
    path('api/createSurvey/', views.apiCreateSurvey, name='apiCreateSurvey'),
    #IMPORT MORE URLS   
    path('contact/', include('apps.contact.urls')),
    path('division/', include('apps.division.urls')),
    path('form/', include('apps.form.urls')),
    path('question/', include('apps.question.urls')),
    path('salesPoint/', include('apps.salesPoint.urls')),
    path('zone/', include('apps.zone.urls'))

]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)