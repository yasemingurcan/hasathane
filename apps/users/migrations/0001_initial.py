# Generated by Django 3.0.7 on 2020-06-14 20:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BaseOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_total', models.DecimalField(decimal_places=2, max_digits=30)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('total', models.DecimalField(decimal_places=2, max_digits=30)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('cargo_company', models.CharField(max_length=20)),
                ('tracking_link', models.TextField()),
                ('status', models.CharField(choices=[('ready', 'Ready'), ('preparing', 'Preparing'), ('delivered', 'Delivered'), ('shipped', 'Shipped')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recognized', models.CharField(choices=[(0, 'Unrecognized'), (1, 'Guest'), (2, 'Registered')], help_text='Designates the state the customer is recognized as.', max_length=20)),
                ('last_access', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last accessed')),
                ('phone', models.CharField(max_length=12)),
                ('password', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=19)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite', to='users.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('favorite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='users.Favorite')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
            ],
        ),
        migrations.CreateModel(
            name='BaseOrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, help_text='Product name at the moment of purchase.', max_length=255, null=True, verbose_name='Product name')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=30, null=True, verbose_name='Unit Price')),
                ('unit', models.CharField(max_length=10)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='users.BaseOrder', verbose_name='Order')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Product', verbose_name='Product')),
            ],
        ),
        migrations.AddField(
            model_name='baseorder',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='users.Customer', verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='baseorder',
            name='products',
            field=models.ManyToManyField(through='users.BaseOrderItems', to='products.Product'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('province', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Customer')),
            ],
        ),
    ]
