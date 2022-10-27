from django.contrib import admin
from .models import Quotation, QuotationItem


# class QuotationInline(admin.TabularInline):
#     model = Quotation
#     extra = 0
#     show_change_link = True


class QuotationItemInline(admin.StackedInline):
    model = QuotationItem
    extra = 1
    fields = ('space', 'layer1', 'layer2', 'work', 'vendor_work', 'amount', 'weighting', 'price_display')
    readonly_fields = ('price', 'price_display')
    # list_display = ['work']

# Register your models here.


@admin.register(Quotation)
class QuotationAdmin(admin.ModelAdmin):
    list_display = ['case', 'version', 'quote_date', 'items_count', 'final_price']
    inlines = [QuotationItemInline]

    def items_count(self, instance):
        return instance.items.count()
    items_count.short_description = '項目數'

    def sum_price(self, instance):
        sum = 0
        items = instance.items.all()
        for item in items:
            sum += item.amount * item.work.unit_price

        return f"$ {sum}"
    sum_price.short_description = '總價'


@admin.register(QuotationItem)
class QuotationItemAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name']
    # inlines = [QuotationItemInline]
