from django.contrib import admin
from .models import Customer, Case, CaseSpace


class CaseSpaceInline(admin.StackedInline):
    model = CaseSpace
    extra = 0


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    inlines = [CaseSpaceInline]
    pass
