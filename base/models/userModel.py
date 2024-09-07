from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from base.models.addressModel import Address
from base.models.cartItemModel import CartItem

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, max_length=255, blank=False)
    first_name = models.CharField("first name", max_length=150,)
    last_name = models.CharField("last name", max_length=150,)
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField("active", default=False)
    is_superuser = models.BooleanField("superuser", default=False)
    date_joined = models.DateTimeField("date joined", default=timezone.now)
    phone = models.CharField(unique=True, max_length=12, blank=False)
    is_business = models.BooleanField(default=False)
    additional_discount = models.IntegerField(default=0, blank=True)
    addresses = models.ManyToManyField(Address, related_name="addresses",blank=True)
    cart = models.ManyToManyField(CartItem, related_name="cart")

    USERNAME_FIELD = "email"
    objects = UserManager()

    def __str__(self):
        return self.email

    def full_name(self):
        return self.first_name + " " + self.last_name

    def get_all_users(self):
        return User.objects.all()

    def get_user_by_email(self, email):
        return User.objects.get(email=email)

    def update_user(self, active, is_business, additional_discount):
        self.is_active = active
        self.is_business = is_business
        self.additional_discount = additional_discount
        self.save()
        return self

    def remove_user(self):
        self.delete()

    def get_cart_by_user_and_product(self, product):
        try:
            return self.cart.get(product=product)
        except CartItem.DoesNotExist:
            return None

    def add_to_cart(self, product,ib):
        p = product.businessPrice if ib else product.price
        d = p - p * product.discount / 100
        return CartItem.objects.create(
            product=product,
            quantity=1,
            totalPrice=round(p),
            discountedPrice=round(d - d * self.additional_discount / 100)  # type:ignore
        )

    def update_cart(self, cart, quantity):
        cart.quantity = quantity
        p = cart.product.businessPrice if self.is_business else cart.product.price
        cart.totalPrice = round(p * quantity)
        d = p - p * cart.product.discount / 100
        cart.discountedPrice = (
            round(d - d * self.additional_discount / 100) * quantity
        )  # type:ignore
        cart.save()
        return cart

    def create_address(self, address, city, state, pincode):
        return self.addresses.add(
            Address.objects.create(
                address=address,
                city=city,
                state=state,
                pincode=pincode,
            )
        )
    
    def remove_address(self, id):
        return Address.objects.get(id=id).delete()