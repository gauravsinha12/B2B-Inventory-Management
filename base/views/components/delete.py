from django.contrib import messages
from django.shortcuts import redirect
from base.models.enquiryModel import Enquiry
from base.models.orderModel import Order
from base.models.productsModel import Brand, Category, Products
from base.views.Htmx import HtmxHttpRequest

#delete Product
def delete_product(request:HtmxHttpRequest):
    if not request.user.is_superuser:redirect("") #type:ignore
    if not request.POST: redirect("")
    try:
        product=Products().get_product_by_id(int(request.POST["productID"]))
        messages.success(request,f"Deleted Product {product.name}")
        product.delete()
    except:
        messages.success(request,f"Product wasn't be deleted")
    return redirect("admin_products")

def delete_order(request:HtmxHttpRequest):
    if not request.user.is_superuser:redirect("") #type:ignore
    if not request.POST: redirect("")
    try:
        order = Order().get_order_by_id(int(request.POST["orderID"]))
        messages.success(request,f"Deleted Order")
        order.delete()
    except:
        messages.success(request,f"Order wasn't be deleted")
    return redirect("admin_orders")

def delete_enquiry(request:HtmxHttpRequest):
    if not request.user.is_superuser:redirect("") #type:ignore
    if not request.POST: redirect("")
    try:
        enquiry = Enquiry().get_enquiry_by_id(int(request.POST["enquiryID"]))
        messages.success(request,f"Deleted Enquiry")
        enquiry.delete()
    except:
        messages.success(request,f"Enquiry wasn't be deleted")
    return redirect("admin_enquiries")

def delete_brand(request:HtmxHttpRequest):
    if not request.user.is_superuser:redirect("") #type:ignore
    if not request.POST: redirect("")
    try:
        brand = Brand().get_brand_by_id(int(request.POST["brandID"]))
        messages.success(request,f"Deleted Brand {brand.name}")
        brand.delete()
    except:
        messages.success(request,f"Brand wasn't be deleted")
    return redirect("admin_brands")

def delete_category(request:HtmxHttpRequest):
    if not request.user.is_superuser:redirect("") #type:ignore
    if not request.POST: redirect("")
    try:
        category = Category().get_category_by_id(int(request.POST["categoryID"]))
        messages.success(request,f"Deleted Category {category.name}")
        category.delete()
    except:
        messages.success(request,f"Category wasn't be deleted")
    return redirect("admin_categories")