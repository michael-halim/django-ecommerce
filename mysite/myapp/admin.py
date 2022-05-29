from django.contrib import admin
from .models import Product
# Register your models here.

admin.site.site_header = 'Buy & Sell Website'
admin.site.site_title = 'ABC Buy'
admin.site.index_title = 'Manage ABC Buying Website'

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','price','desc')
    search_fields = ('name','price')
    actions = ('set_price_to_zero',)

    def set_price_to_zero(self, request, queryset):
        queryset.update(price=0)

    list_editable = ('price','desc')


admin.site.register(Product,ProductAdmin)