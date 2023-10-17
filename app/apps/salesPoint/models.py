from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.contrib.auth.models import User

from apps.zone.models import Zone
from apps.division.models import Division

class SalesPoint(models.Model):
    PROVINCE = (
        ('SJO','San Jose'),
        ('ALA','Alajuela'),
        ('CAR','Cartago'),
        ('HER','Heredia'),
        ('GUA','Guatemala'),
        ('PUN','Puntarenas'),
        ('LIM','Limon'),
    )     
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE)
    name = models.CharField(max_length=75)
    province = models.CharField(max_length=11, choices=PROVINCE, null=True)
    canton = models.CharField(max_length=75)
    district = models.CharField(max_length=75)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    lngNode = models.CharField(max_length=11, default="-84.0833")
    latNode = models.CharField(max_length=11, default="9.93333")
    users = models.ManyToManyField(User, blank=True)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SalesPoint,self).save(*args,**kwargs)

    def __str__(self):
        return self.name