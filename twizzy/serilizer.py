from rest_framework import serializers
from .models import product 
class Product_serilizer(serializers.ModelSerializer):
    class Meta:
        model=product
        fields='__all__'