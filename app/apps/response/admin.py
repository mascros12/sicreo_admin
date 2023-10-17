from django.contrib import admin
from .models import Response

class ResponseAdmin(admin.ModelAdmin):
    fields = ('survey', 'question', 'response')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Response, ResponseAdmin)