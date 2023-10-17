from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

from apps.survey.models import Survey
from apps.question.models import Question

class Response(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response = models.SmallIntegerField()

    slug = models.SlugField(null=False, blank=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.survey.bill_id) + "_" + str(self.question.id))
        super(Response,self).save(*args,**kwargs)

    def __str__(self):
        return self.survey + self.question
