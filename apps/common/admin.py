from django.contrib import admin

# Register your models here.
from apps.common.models import HomePage, Footer


@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'order']


@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ['name', 'link', 'section', 'order']
