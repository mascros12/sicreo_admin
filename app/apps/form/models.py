from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.division.models import Division

class Form(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField(null=True, blank=True)
    division = models.ManyToManyField(Division, blank=True)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Form,self).save(*args,**kwargs)

    def __str__(self):
        return self.name
