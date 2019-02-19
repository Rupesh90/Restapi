from django.shortcuts import render
from rest_framework import viewsets
from .models import FlipModel,Product
from .serializers import FlipVendorSerializer,FlipProductsSerializers

# Create your views here.


class FlipVendorRead(viewsets.ReadOnlyModelViewSet):
    queryset = FlipModel.objects.all()
    serializer_class = FlipVendorSerializer

class FlipProductsCrud(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = FlipProductsSerializers

class FlipVendorCrud(viewsets.ModelViewSet):
    queryset = FlipModel.objects.all()
    serializer_class = FlipVendorSerializer
