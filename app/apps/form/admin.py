from django.contrib import admin
from .models import Form

class FormAdmin(admin.ModelAdmin):
    fields = ('name', 'description', 'division',)
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Form, FormAdmin)
