from django.db import models

# Create your models here.
class Messages(models.Model):
    user = models.CharField(max_length=200)
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
