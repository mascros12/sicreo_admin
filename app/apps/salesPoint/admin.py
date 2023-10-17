from django.contrib import admin
from .models import SalesPoint

class SalesPointAdmin(admin.ModelAdmin):
    fields = ('zone', 'name', 'province', 'canton', 'district', 'division')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(SalesPoint, SalesPointAdmin)