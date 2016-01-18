from django.contrib import admin
from .models import Category, Product, Store, Quotation


class QuotationAdmin(admin.ModelAdmin):
    list_display = ('id', 'store', 'product', 'price', 'quantity')


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Store)
admin.site.register(Quotation, QuotationAdmin)
