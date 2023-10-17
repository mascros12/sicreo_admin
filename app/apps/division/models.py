from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Division(models.Model):
   name = models.CharField(max_length=100)
   logo = models.ImageField(upload_to="division/",null=True, blank=True)
   logo_white = models.ImageField(upload_to="division/",null=True, blank=True)

   slug = models.SlugField(null=False, blank=False, unique=True)
   created_at = models.DateTimeField(auto_now_add=True)

   def save(self, *args, **kwargs):
       self.slug = slugify(self.name)
       super(Division,self).save(*args,**kwargs)

   def __str__(self):
       return self.name