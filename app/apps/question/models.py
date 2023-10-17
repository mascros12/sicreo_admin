from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
import secrets

from apps.form.models import Form
from apps.division.models import Division

class Question(models.Model):
    TYPE = (
        (2,'Pregunta de Si/No'),
        (5,'Pregunta escala del 1-5')
    )   
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    division = models.ManyToManyField(Division, blank=True)
    question = models.CharField(max_length=250)
    qty_responses = models.SmallIntegerField(choices=TYPE)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(secrets.token_urlsafe(16))
        super(Question,self).save(*args,**kwargs)

    def __str__(self):
        return self.question