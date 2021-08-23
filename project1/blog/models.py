from django.db import models

# Create your models here.
class Blog (models.Model):
    #id = primaryKey (django creates the id by default)
    author = models.CharField(max_length=255, null=False)
    description = models.TextField()