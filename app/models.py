from django.db import models

class Header(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(max_length=255)

class About(models.Model):
    name = models.CharField(max_length=255)
    job = models.CharField(max_length=255)

class Service(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(max_length=255)