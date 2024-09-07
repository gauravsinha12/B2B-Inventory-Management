from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from base.forms import ProductForm, CategoryForm, BrandForm,AddressForm
from base.models import Category, Brand, Products
from base.views.Htmx import HtmxHttpRequest, renderX

products = Products()
categories = Category()
brands = Brand()


# Edit Product
def edit_product(request: HtmxHttpRequest, id) -> HttpResponse:
    if not request.user.is_superuser:# type:ignore
        return redirect("home")  
    product = products.get_product_by_id(id)
    if not product:
        return redirect("admin_products")
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Product Updated Successfully")
            return redirect("admin_products")
    errors = form.errors
    form = ProductForm(instance=product)
    return renderX(
        request,
        "admin/add.html",
        {"form": form, "url": f"/admin/edit-product/{id}", "errors": errors},
    )


# Edit Category
def edit_category(request: HtmxHttpRequest, id) -> HttpResponse:
    if not request.user.is_superuser:# type:ignore
        return redirect("home")  
    category = categories.get_category_by_id(id)
    if not category:
        return redirect("admin_categories")
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, "Category Updated Successfully")
            return redirect("admin_categories")
    errors = form.errors
    form = CategoryForm(instance=category)
    return renderX(
        request,
        "admin/add.html",
        {"form": form, "url": f"/admin/edit-category/{id}", "errors": errors},
    )


# Edit Brand
def edit_brand(request: HtmxHttpRequest, id) -> HttpResponse:
    if not request.user.is_superuser:# type:ignore
        return redirect("home")  
    brand = brands.get_brand_by_id(id)
    if not brand:
        return redirect("admin_brands")
    form = BrandForm()
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand Updated Successfully")
            return redirect("admin_brands")
    errors = form.errors
    form = BrandForm(instance=brand)
    return renderX(
        request,
        "admin/add.html",
        {"form": form, "url": f"/admin/edit-brand/{id}", "errors": errors},
    )

def edit_address(request:HtmxHttpRequest):
    if request.user.is_authenticated:
        if request.POST:
            address_id = request.POST["address_id"]
            address = request.user.addresses.get(id=address_id) #type:ignore
            form = AddressForm(request.POST, instance=address)
            if form.is_valid():
                form.save()
                messages.success(request, "Address updated successfully")
                return redirect(request.META['HTTP_REFERER'])
            else:
                messages.error(request, "Address cannot be updated!")
                return redirect(request.META['HTTP_REFERER'])
        else:
            messages.error(request, "Address cannot be updated!")
            return redirect(request.META['HTTP_REFERER'])
    return redirect("signin")