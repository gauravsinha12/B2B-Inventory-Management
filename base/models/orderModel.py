from django.db import models
from base.models.constants import Consants
from base.models.productsModel import Products
from base.models.addressModel import Address
from django.utils import timezone

from base.models.userModel import User


class Order(models.Model):
    address = models.ForeignKey(
        Address,
        related_name="orderaddress",
        on_delete=models.SET_NULL,
        null=True,
        unique=False,
    )
    status = models.IntegerField(
        choices=Consants.OrderStatusChoices, default=Consants.IN_PROCESS
    )
    product = models.ForeignKey(
        Products, related_name="orderProduct", on_delete=models.CASCADE, null=True
    )
    quantity = models.IntegerField(blank=False,default=0)
    totalPrice = models.IntegerField(blank=False,default=0)
    discountedPrice=models.IntegerField(blank=False,default=0)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name="user",on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.product.name  # pyright:ignore[reportOptionalMemberAccess]

    def get_order_by_id(self, id):
        return Order.objects.get(id=id)
    
    def get_all_order_by_filters(self, status=None, product=None,user=None):
        if status and product:
            return Order.objects.filter(status__in=status, product=product)
        elif status:
            return Order.objects.filter(status__in=status)
        elif product:
            return Order.objects.filter(product=product)
        elif status and user:
            return Order.objects.filter(status__in=status,user=user)
        else:
            return Order.objects.all()

    def create_order(self, address,user, status, item):
        return Order.objects.create(
                user=user,
                address=address,
                status=status,
                product=item.product,
                quantity=item.quantity,
                totalPrice=item.totalPrice,
                discountedPrice=item.discountedPrice,
            )
    
    def cancel_an_order(self, id):
        order = Order.objects.get(id=id)
        order.product.inventory += order.quantity # type:ignore
        order.product.save() # type:ignore
        order.status = 5
        order.save()
        return order
    
    def update_order_status(self, id, status):
        order = Order.objects.get(id=id)
        order.status = status
        order.save()
        return order