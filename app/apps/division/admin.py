from django.contrib import admin
from .models import Division

class DivisionAdmin(admin.ModelAdmin):
    fields = ('name', 'logo', 'logo_white')
    list_display = ('__str__', 'created_at')

admin.site.register(Division, DivisionAdmin)
