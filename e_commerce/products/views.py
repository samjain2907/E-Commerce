from django.shortcuts import render
from products.models import Product
from rest_framework.generics import ListAPIView , RetrieveAPIView
from products.serializers import ProductSerializer

# Create your views here.
class productallview(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class producteachview(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
