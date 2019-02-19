from rest_framework import serializers
from .models import FlipModel,Product

class FlipVendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlipModel
        fields = '__all__'

class FlipProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'