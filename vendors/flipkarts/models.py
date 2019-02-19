from django.db import models

# Create your models here.
class FlipModel(models.Model):
    #flipid = models.CharField(max_length=20)
    flipName = models.CharField(max_length=100)
    flipBalance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table = "Vendor1"


class Product(models.Model):
   # productId = models.CharField(max_length=20)
    productName = models.CharField(max_length=100)
    productPrice = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    productQty = models.IntegerField()
    fliProducts = models.ForeignKey(FlipModel,on_delete=models.CASCADE)

    class Meta:
        db_table = "Product1"
