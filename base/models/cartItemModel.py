from django.db import models
from django.utils import timezone

from base.models.productsModel import Products

class CartItem(models.Model):
    product = models.ForeignKey(
        Products, related_name="cartproduct", on_delete=models.CASCADE
        )
    quantity = models.IntegerField(blank=False)
    totalPrice = models.IntegerField(blank=False)
    discountedPrice=models.IntegerField(blank=False,default=0) # type: ignore
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.name  # pyright:ignore[reportOptionalMemberAccess]