from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ('form', 'question', 'qty_responses', 'division')
    list_display = ('__str__', 'slug', 'created_at')

admin.site.register(Question, QuestionAdmin)