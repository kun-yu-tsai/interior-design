from django.contrib import admin
from .models import Provider, ProviderWork


class ProviderWorkInline(admin.TabularInline):
    model = ProviderWork
    extra = 0


# @admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ['name']


# @admin.register(ProviderWork)
class ProviderWorkAdmin(admin.ModelAdmin):
    list_display = ['work', 'unit_price', 'note', 'active']
