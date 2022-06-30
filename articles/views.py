from django.shortcuts import render
from django.db import models

# Create your views here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()