from django.db import models
import datetime

# Create your models here.

class Show(models.Model):
    show_name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    show_date = models.DateField('date of show', default=datetime.datetime.now)
    video_url = models.CharField(max_length=300, default=None, blank=True, null=True)

    def __str__(self):
        return self.description
