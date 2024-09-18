from rest_framework import viewsets , filters # type: ignore
from .serializers import ProductSerializer , RateSerializer # type: ignore
from .models import Product , Rate

class all_products(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backend=[filters.SearchFilter]
    search_fields=['title']
    
        
class product_rates(viewsets.ModelViewSet):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    

    
    
    