from django.contrib import admin
from .models import *

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'price']
class SubCategoryAdmin(admin.ModelAdmin):
    list_display =['id', 'short_name', 'main_category']

class SalesCategorieAdmin(admin.ModelAdmin):
    list_display =['id', 'short_name']

class MenuItemsAdmin(admin.ModelAdmin):
    list_display =['id', 'short_name','collecion_category']

class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone', 'date', 'paid']
    list_filter = ('id','requested','paid' )


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'dep', 'short_name', 'description']

class LineItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'date_added', 'order']

class DepartmentAdvertsAdmin(admin.ModelAdmin):

    # fieldsets = [
    #     (None, {'fields': ['reference','qrCode','picture','location','deliveryAddress','unitNumber','package_user','available','valid']}),
    # ]
    list_display = ('title','product','category','dep','published_date','expire_date','isActive')
    list_filter = ('title','isActive')

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(CartItem, OrderItemAdmin)
admin.site.register(LineItem, LineItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(SalesCategorie,SalesCategorieAdmin)
admin.site.register(MenuItems,MenuItemsAdmin)
admin.site.register(MainMenuAds)
admin.site.register(Collection_Banner)
admin.site.register(DepartmentAdverts, DepartmentAdvertsAdmin)
admin.site.register(ProductAdverts)
admin.site.register(ProductMaterialMainColor)