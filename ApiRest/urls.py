from django.urls import path , include
from . import  views
from rest_framework.routers import DefaultRouter  # type:ignore



router=DefaultRouter()
router.register('products' ,views.all_products)
router.register('products_rates' ,views.product_rates)


urlpatterns = [
    path('', include(router.urls))
]
