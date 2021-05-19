from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=120,null=True,blank=True)
    desc = models.CharField(max_length=250,null=True,blank=True)
    