from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

class Contact(models.Model): 
    contact_id = models.CharField(max_length=35)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    full_name = models.CharField(max_length=151)
    phone = models.CharField(max_length=25, null=True, blank=True)
    mobile = models.CharField(max_length=25, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    employee = models.BooleanField(null=True, blank=True)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.full_name = self.first_name + " " + self.last_name
        self.slug = slugify(self.full_name)
        super(Contact,self).save(*args,**kwargs)

    def __str__(self):
        return self.full_name
