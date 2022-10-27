from django.contrib import admin
from .models import SpaceType, SpaceName


@admin.register(SpaceType)
class SpaceTypeAdmin(admin.ModelAdmin):
    pass

@admin.register(SpaceName)
class SpaceNameAdmin(admin.ModelAdmin):
    pass