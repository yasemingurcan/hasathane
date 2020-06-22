from django.db import models

from .choices import UNIT_CHOICES, CURRENCY_CHOICES
from django.utils.translation import gettext_lazy as _

# Create your models here.
from ..common.models import Brand


class BaseProperty(models.Model):
    name = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='children',
        on_delete=models.CASCADE
    )
    properties = models.ManyToManyField(BaseProperty, blank=True, null=True)

    class Meta:
        # enforcing that there can not be two categories under a parent with same slug

        # __str__ method elaborated later in post.  use __unicode__ in place of

        # __str__ if you are using python 2

        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, null=True, blank=True, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    amount = models.DecimalField(max_digits=5, decimal_places=3, null=True, blank=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES, null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, null=True)
    description = models.TextField(null=True, blank=True)
    meta_data = models.TextField(null=True, blank=True)
    is_returnable = models.BooleanField(default=True)
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )

    active = models.BooleanField(
        _("Active"),
        default=True,
        help_text=_("Is this product publicly visible."),
    )
