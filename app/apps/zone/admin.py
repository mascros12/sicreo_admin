from django.contrib import admin
from .models import Zone

class ZoneAdmin(admin.ModelAdmin):
    fields = ('name', 'manager')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Zone, ZoneAdmin)
