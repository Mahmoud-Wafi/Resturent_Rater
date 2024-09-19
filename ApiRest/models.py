from decimal import Decimal

from django.db.models import Avg , Count
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    CATEGORIES = [
        ("Fast Food", "Fast Food"),
        ("Casual Dining", "Casual Dining"),
        ("Fine Dining", "Fine Dining"),
        ("Cafés", "Cafés"),
        ("Buffets", "Buffets"),
    ]
    
    title = models.CharField(max_length=30, unique=True, blank=True, null=True)
    description = models.TextField(max_length=150, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=40, choices=CATEGORIES)

    def __str__(self):
        return self.title
    @property
    def discount(self):
        discount_rate = Decimal('0.1')
        discount_amount = self.price * discount_rate  
        discounted_price = self.price - discount_amount 
        return round(discounted_price, 2)
    @property
    def average_rating(self):
        return Rate.objects.filter(product=self).aggregate(Avg('stars'))#['stars__avg'] or 0.0
    @property
    def Reviews(self):
        return Rate.objects.filter(product=self).count()


class Rate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    def __str__(self):
        return f"{self.product.title} rated by {self.user.username}"

    class Meta:
        unique_together = [("user", "product")]  # User can't rate the same product twice
        indexes = [
            models.Index(fields=['user', 'product']),  # Create an index for efficient queries
        ] 
