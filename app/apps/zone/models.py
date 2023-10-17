from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

from apps.contact.models import Contact

class Zone(models.Model):   
    name = models.CharField(max_length=100, unique=True)
    manager = models.ForeignKey(Contact, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Zone,self).save(*args,**kwargs)

    def __str__(self):
        return self.name