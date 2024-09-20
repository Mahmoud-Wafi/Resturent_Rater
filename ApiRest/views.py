from rest_framework import viewsets , filters # type: ignore
from .serializers import ProductSerializer , RateSerializer # type: ignore
from .models import Product , Rate
from rest_framework.decorators import action # type: ignore
from rest_framework import status                 # type: ignore
from rest_framework.response import Response            # type: ignore
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication  # type: ignore
class all_products(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backend=[filters.SearchFilter]
    search_fields=['title']
    authentication_classes=(TokenAuthentication,)


    @action(methods=['POST'], detail=True)
    def add_rate(self, request, pk):
        stars = request.data.get('stars')
        # username = request.data.get('username')
        user=request.user
        if stars is None or user is None:
            return Response({"message": "Stars and username must be provided"}, status=status.HTTP_400_BAD_REQUEST)
        if not (1 <= stars <= 5):
            return Response({"message": "Stars must be between 1 and 5"}, status=status.HTTP_400_BAD_REQUEST)
        product = get_object_or_404(Product, id=pk)
        user = get_object_or_404(User, username=user)
        rate, created = Rate.objects.update_or_create(
            user=user,
            product=product,
            defaults={'stars': stars}
        )
        serializer = RateSerializer(rate)
        if created:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_200_OK)

class product_rates(viewsets.ModelViewSet):
    queryset=Rate.objects.all()
    serializer_class=RateSerializer
    authentication_classes=(TokenAuthentication,)
    
    
    def update(self, request,*args,**kwargs):
        response={
            "message":"Not Authorized to create or update"
        }
    
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
    def create(self, request,*args,**kwargs):
        response={
            "message":"Not Authorized to create or update"
        }
    
        return Response(response,status=status.HTTP_400_BAD_REQUEST)
 
    
    
    