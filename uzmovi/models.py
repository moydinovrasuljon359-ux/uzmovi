from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to='media/' , null=True, blank=True) 
    qoshimcha = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name