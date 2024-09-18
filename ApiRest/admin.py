from django.contrib import admin
from .models import Product , Rate


class ProductAdmin(admin.ModelAdmin):
    list_display=["id","title","description","price","category","discount","average_rating"]
    search_fields=["title","price","category"]
    list_filter=["title","price","category"]
class RateAdmin(admin.ModelAdmin):
    list_display=["id","user","product","stars"]
    list_filter=["user","product"]
    
    
    
admin.site.register(Product , ProductAdmin)
admin.site.register(Rate , RateAdmin)
# Register your models here.
