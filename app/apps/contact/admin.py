from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    fields = ('contact_id', 'first_name', 'last_name', 'mobile', 'phone', 'email', 'employee')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Contact, ContactAdmin)