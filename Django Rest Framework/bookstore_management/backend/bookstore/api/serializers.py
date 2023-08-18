from rest_framework import serializers
from .models import BookStoreModel

class BookStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookStoreModel
        fields = '__all__'