# Generated by Django 3.0.7 on 2020-06-18 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footer',
            name='section',
            field=models.SmallIntegerField(),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='type',
            field=models.CharField(choices=[('slider', 'Slider'), ('benefit', 'Benefit'), ('category', 'Category'), ('special', 'Special')], max_length=30),
        ),
    ]