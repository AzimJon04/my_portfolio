from django.db import models

# Create your models here.


class About_me(models.Model):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)

    def __str__(self):
        return self.first_name


class My_contact(models.Model):
    phone = models.BigIntegerField(blank=True, null=True)
    telegram = models.URLField(blank=True)
    email = models.EmailField(max_length=255)
    linkedin = models.URLField(blank=True)
    github = models.URLField(blank=True)


class Portfolio(models.Model):
    title = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='images/', blank=True)
    description = models.TextField(blank=True)
    description_ru = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
