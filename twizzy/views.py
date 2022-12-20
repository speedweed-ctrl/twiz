from django.shortcuts import render
from .models import product
from .serilizer import Product_serilizer
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def get_products(request):
    data=product.objects.all()
    serilizer=Product_serilizer(data,many=True)
    return Response(serilizer.data)
