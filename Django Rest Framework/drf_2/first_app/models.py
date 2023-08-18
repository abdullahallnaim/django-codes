from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2) # 120.65
    def __str__(self):
        return self.name

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # obj kkhn toiri hoiche setar time save korbe
    updated_at = models.DateTimeField(auto_now=True) # user jkhn review edit korbe tokhn time ta dekhabe
    class Meta:
        unique_together = ('product', 'user') # ekjon user jeno ektai comment korte pare sejonne ei line ta
        
    def __str__(self):
        return f"{self.user.username} - {self.product.name} - Rating: {self.rating}"
