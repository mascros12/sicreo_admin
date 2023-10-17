from django.contrib import admin
from .models import Survey

class SurveyAdmin(admin.ModelAdmin):
    fields = ('sales_point', 'contact', 'form', 'bill_id', 'date')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Survey, SurveyAdmin)