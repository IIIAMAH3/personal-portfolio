import datetime
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today())
    description = models.TextField()


    def __str__(self):
        return self.title