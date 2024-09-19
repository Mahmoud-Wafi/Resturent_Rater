from rest_framework import serializers # type: ignore
from .models import Product, Rate

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','description','category','price','discount','average_rating','Reviews']

    def validate(self, data):
        if data['price'] <= 20:
            raise serializers.ValidationError({"price": "Price must be greater than Twenty."})
       
        if not data.get('title'):
            raise serializers.ValidationError({"title": "Title is required."})
        return data
class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = "__all__"
        
    def validate(self, data):
        if data['stars'] < 1 or data['stars'] > 5:
            raise serializers.ValidationError({"stars": "Stars must be between 1 and 5."})
        if Rate.objects.filter(user=data['user'], product=data['product']).exists():
            raise serializers.ValidationError({"product": "You have already rated this product."})
        return data
