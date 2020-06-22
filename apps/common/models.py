from django.db import models
from .choices import FOOTER_TYPE_CHOICES, HOMEPAGE_TYPE


# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField()
    address = models.TextField()


class Brand(models.Model):
    name = models.CharField(max_length=200)
    meta_data = models.TextField(null=True, blank=True)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    # image


class Footer(models.Model):
    name = models.CharField(max_length=200)
    link = models.TextField(null=True, blank=True)
    section = models.SmallIntegerField()
    order = models.SmallIntegerField()


class FooterItem(models.Model):
    footer = models.ForeignKey(Footer, on_delete=Footer)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=15, choices=FOOTER_TYPE_CHOICES)
    order = models.SmallIntegerField()
    link = models.TextField(null=True, blank=True)
    # image


class HomePage(models.Model):
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=30, choices=HOMEPAGE_TYPE)
    order = models.SmallIntegerField()


class MainMenuItem(models.Model):
    display_name = models.CharField(max_length=200)
    order = models.SmallIntegerField()
    link = models.TextField(null=True, blank=True)
