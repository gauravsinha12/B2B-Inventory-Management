from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.db import models
from base.models.constants import Consants

class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    image = CloudinaryField(overwrite=True,null=True)

    def __str__(self):
        return self.name
    
    def get_all_category(self):
        return Category.objects.all()
    
    def get_category_by_id(self, id):
        return Category.objects.get(id=id)


class Brand(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    image = CloudinaryField(overwrite=True,null=True)

    def __str__(self):
        return self.name
    
    def get_all_brand(self):
        return Brand.objects.all()
    
    def get_brand_by_id(self, id):
        return Brand.objects.get(id=id)


class Products(models.Model):
    name = models.CharField(max_length=255, blank=False)
    description = models.TextField()
    price = models.IntegerField(blank=False)
    businessPrice = models.IntegerField(blank=False, default=0)
    discount = models.IntegerField(default=0)
    inventory = models.IntegerField(blank=False, default=0)
    packOf = models.IntegerField(blank=False,default=0)
    inCase = models.IntegerField(blank=False,default=0)
    image1 = CloudinaryField(overwrite=True,null=True)
    image2 = CloudinaryField(null=True,blank=True,overwrite=True)
    image3 = CloudinaryField(null=True,blank=True,overwrite=True)
    image4 = CloudinaryField(null=True,blank=True,overwrite=True)
    video = models.URLField(blank=True,null=True)
    category = models.ForeignKey(
        Category, related_name="category", on_delete=models.CASCADE
    )
    brand = models.ForeignKey(Brand, related_name="brand", on_delete=models.CASCADE)
    visibility = models.IntegerField(
        choices=Consants.VisiblityChoices, default=Consants.NONE
    )
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_all_products(self):
        return Products.objects.all()
    
    def filter_by_visibility(self, visibility):
        return Products.objects.filter(visibility=visibility)

    def filter_by_category(self, category):
        return Products.objects.filter(category=category)

    def filter_by_brand(self, brand):
        return Products.objects.filter(brand=brand)

    def filters_by_category_and_brand(self, category, brand):
        return Products.objects.filter(category=category, brand=brand)

    def get_product_by_id(self, id):
        return Products.objects.get(id=id)

    def add_or_update_product(
        self,
        name,
        description,
        price,
        businessPrice,
        discount,
        inventory,
        image1,
        image2,
        image3,
        image4,
        video,
        category,
        brand,
        featured,
        visibility,
        update=False,
    ):
        if update:
            self.name = name
            self.description = description
            self.price = price
            self.businessPrice = businessPrice
            self.discount = discount
            self.inventory = inventory
            self.image1 = image1
            self.image2 = image2
            self.image3 = image3
            self.image4 = image4
            self.video = video
            self.category = category
            self.brand = brand
            self.featured = featured
            self.visibility = visibility
            self.save()
            return self
        else:
            return Products.objects.create(
                name=name,
                description=description,
                price=price,
                businessPrice=businessPrice,
                discount=discount,
                inventory=inventory,
                image1=image1,
                image2=image2,
                image3=image3,
                image4=image4,
                video=video,
                category=category,
                brand=brand,
                featured=featured,
                visibility=visibility,
            )

    def remove_product(self):
        self.delete()