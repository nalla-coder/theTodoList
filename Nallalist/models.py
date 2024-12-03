from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length = 55)
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    description = models.TextField()

# class Category(models.Model):
#     name = models.CharField(max_length = 100)

# class Tasks(models.Model):
#     name = models.CharField(max_length = 100) 

# Create your models here.
def __str__(self):
    return self.title + "-" + str(self.author)

def get_abosolute_urls(self):
    return reverse("post-details", args = [str(self.id)]) 

