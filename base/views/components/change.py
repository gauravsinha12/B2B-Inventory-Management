from django.http import HttpResponse
from django.shortcuts import redirect
from base.models.productsModel import Products
from base.models import User,Order
from base.views.Htmx import HtmxHttpRequest

users = User()
orders=Order()

def change_visibility(request:HtmxHttpRequest)->HttpResponse:
    if not request.user.is_superuser: return redirect("home")  # type: ignore
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        visibility = request.POST.get("visibility")
        product = Products().get_product_by_id(product_id)
        product.add_or_update_product(
            product.name,
            product.description,
            product.price,
            product.businessPrice,
            product.discount,
            product.inventory,
            product.image1,
            product.image2,
            product.image3,
            product.image4,
            product.video,
            product.category,
            product.brand,
            product.featured,
            visibility,
            update=True,
        )
        return redirect("admin_products")
    return redirect("home")

def change_featured(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser: # type: ignore
        return redirect("home")
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        product = Products().get_product_by_id(product_id)
        featured = not product.featured
        product.add_or_update_product(
            product.name,
            product.description,
            product.price,
            product.businessPrice,
            product.discount,
            product.inventory,
            product.image1,
            product.image2,
            product.image3,
            product.image4,
            product.video,
            product.category,
            product.brand,
            featured,
            product.visibility,
            update=True,
        )
        return redirect("admin_products")
    return redirect("home")

def change_user_active(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser: # type: ignore
        return redirect("home") 
    if not request.method == "POST":
        return redirect("home")
    user = users.get_user_by_email(request.POST.get("user"))
    active = not user.is_active
    user.update_user(
        active=active,
        is_business=user.is_business,
        additional_discount=user.additional_discount,
    )
    return redirect("admin_users")


def change_is_business(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    if not request.method == "POST":
        return redirect("home")
    user = users.get_user_by_email(request.POST.get("user"))
    is_business = not user.is_business
    user.update_user(
        active=user.is_active,
        is_business=is_business,
        additional_discount=user.additional_discount,
    )
    return redirect("admin_users")


def change_order_status(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    if not request.method == "POST":
        return redirect("home")
    orders.update_order_status( # type: ignore    
        id=int(request.POST.get("id")),  # type: ignore
        status=int(request.POST.get("status")),  # type: ignore
    )
    return redirect("admin_orders")
