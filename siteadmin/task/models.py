from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)
    category = models.TextField(max_length=50)
    date_expiration = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
