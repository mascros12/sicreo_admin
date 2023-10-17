from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.salesPoint.models import SalesPoint
from apps.contact.models import Contact
from apps.form.models import Form

class Survey(models.Model):
    sales_point = models.ForeignKey(SalesPoint, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True)
    form = models.ForeignKey(Form, on_delete=models.CASCADE)
    bill_id = models.CharField(max_length=25)
    date = models.DateTimeField(null=True, blank=True)

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.bill_id)
        super(Survey,self).save(*args,**kwargs)

    def __str__(self):
        return self.bill_id