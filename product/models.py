from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)


    def __str__(self):
        return self.name




