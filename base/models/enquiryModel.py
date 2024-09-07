from django.db import models
from django.utils import timezone
from base.models.productsModel import Products
from base.models.userModel import User

class Enquiry(models.Model):
    message = models.TextField()
    author = models.ForeignKey(
        User, related_name="author", on_delete=models.CASCADE,null=True, blank=True
    )
    product = models.ForeignKey(
        Products, related_name="product", on_delete=models.CASCADE
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    parent = models.ForeignKey("self", related_name="replies", on_delete=models.CASCADE, null=True, blank=True)

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
    
    @property
    def children(self):
        return Enquiry.objects.filter(parent=self)
    
    def __str__(self):
        return self.message
    
    def get_enquiry_by_id(self, id):
        return Enquiry.objects.get(id=id)

    def get_all_enquiry(self):
        return Enquiry.objects.all()

    def get_enquiry_by_user(self, user):
        return Enquiry.objects.filter(author=user)
    
    def get_enquiry_by_product(self, product):
        return Enquiry.objects.filter(product=product)
    
    def get_enquiry_by_user_and_product(self, user, product):
        return Enquiry.objects.filter(author=user, product=product)

    def remove_enquiry(self):
        self.delete()
