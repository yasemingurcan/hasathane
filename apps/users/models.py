from django.db import models
from django.conf import settings
from decimal import Decimal

from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from apps.products.models import Product
from .choices import CUSTOMER_STATE, GENDER_CHOICES
# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    recognized = models.CharField(
        max_length=20,
        choices=CUSTOMER_STATE,
        help_text=_("Designates the state the customer is recognized as."),
    )

    last_access = models.DateTimeField(
        _("Last accessed"),
        default=timezone.now,
    )
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=19, choices=GENDER_CHOICES)
    birth_date = models.DateField(null=True, blank=True)


class Address(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    user = models.ForeignKey(Customer, on_delete=models.CASCADE)


class BaseOrder(models.Model):
    STATUS_CHOICES = (
        ('ready', 'Ready'),
        ('preparing', 'Preparing'),
        ('delivered', 'Delivered'),
        ('shipped', 'Shipped')
    )

    decimalfield_kwargs = {
        'max_digits': 30,
        'decimal_places': 2,
    }
    decimal_exp = Decimal('.' + '0' * decimalfield_kwargs['decimal_places'])

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        verbose_name=_("Customer"),
        related_name='orders',
    )
    product_total = models.DecimalField(**decimalfield_kwargs)
    discount = models.DecimalField(max_digits=7, decimal_places=2)
    total = models.DecimalField(**decimalfield_kwargs)
    address = models.TextField()
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    cargo_company = models.CharField(max_length=20)
    tracking_link = models.TextField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES)
    products = models.ManyToManyField(Product, through='BaseOrderItems')
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )


class BaseOrderItems(models.Model):
    order = models.ForeignKey(
        BaseOrder,
        on_delete=models.PROTECT,
        related_name='items',
        verbose_name=_("Order"),
    )
    product_name = models.CharField(
        _("Product name"),
        max_length=255,
        null=True,
        blank=True,
        help_text=_("Product name at the moment of purchase."),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        verbose_name=_("Product"),
        null=True,
        blank=True,
    )
    amount = models.DecimalField(**BaseOrder.decimalfield_kwargs)
    unit_price = models.DecimalField(
        _("Unit Price"),
        null=True,
        **BaseOrder.decimalfield_kwargs
    )
    unit = models.CharField(max_length=10)


class BaseCard(models.Model):
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='cart'
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )

    class Meta:
        verbose_name = _("Shopping Cart")
        verbose_name_plural = _("Shopping Carts")


class BaseCartItem(models.Model):
    cart = models.ForeignKey(
        BaseCard,
        on_delete=models.CASCADE,
        related_name='items',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )


class Favorite(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='favorite'
    )
    created_at = models.DateTimeField(
        _("Created at"),
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )


class FavoriteItems(models.Model):
    favorite = models.ForeignKey(
        Favorite,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )
    updated_at = models.DateTimeField(
        _("Updated at"),
        auto_now=True,
    )
