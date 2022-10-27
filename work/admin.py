from django.contrib import admin
from .models import Layer1, Layer2, VendorWork, Work, Unit



class Layer2Inline(admin.TabularInline):
    model = Layer2
    extra = 0


class WorkInline(admin.TabularInline):
    model = Work
    extra = 0


@admin.register(Layer1)
class Layer1Admin(admin.ModelAdmin):
    inlines = [Layer2Inline]


@admin.register(Layer2)
class Layer2Admin(admin.ModelAdmin):
    # filter_horizontal = ('layer1',)
    # how to change list filter position
    # https://stackoverflow.com/questions/61382909/shifting-of-filter-section-from-right-sidebar-to-left-side-bar-in-change-list-pa
    # change_list_template= 'change_list_form.html'
    list_display = ['name', 'layer1']
    fields = ['name', 'layer1', ]
    list_filter = ['layer1']
    inlines = [WorkInline]


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    # filter_horizontal = ('layer2',)
    list_display = ['name', 'unit', 'unit_price',
                    'layer1', 'layer2', ]
    # list_filter = ['belong_to']
    fields = ['name', 'unit', 'unit_price', 'layer2', ]

    def layer1(self, instance):
        return instance.layer2.layer1 if instance.layer2 else None
    layer1.short_description = '所屬工程'
    # inlines = [ProviderWorkInline]

@admin.register(VendorWork)
class VendorWorkAdmin(admin.ModelAdmin):
    pass

# @admin.register(Unit)
# class UnitAdmin(admin.ModelAdmin):
#     list_display = ['name', ]
#     pass

    # def specs(self, obj):
    #     return format_html("<br>".join([f'- {spec.spec_name}' for spec in obj.specs.all().order_by('price_per_unit')]))
    # specs.short_description = '規格列'

    # def second_categories(self, obj):
    #     return format_html("<br>".join([f'{cate2.name}' for cate2 in obj.belong_to_second_categories.all().order_by('relations_with_products__product_ordering')]))
    # second_categories.short_description = '所屬小類'

    # search_fields = ('name', 'belong_to_second_categories__name', 'specs__spec_name', 'vendor__name', 'description')
    # list_display = ('name', 'second_categories', 'specs', 'vendor', 'description', 'on_stock',)
    # fields = ('name', 'vendor', 'description', 'on_stock',)
    # inlines = (ProductBelongsToWhichSecCateInline, ProductSpecInline, ProductImageInline, )
