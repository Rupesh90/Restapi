from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FlipModel,Product
# Register your models here.
admin.site.register(FlipModel)
admin.site.register(Product)