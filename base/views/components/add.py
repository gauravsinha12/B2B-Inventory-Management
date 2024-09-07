from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from base.forms import ProductForm, CategoryForm, BrandForm,AddressForm
from base.models import Category, Brand
from base.views.Htmx import HtmxHttpRequest, renderX

categories = Category()
brands = Brand()


def check_none(value):
    if value == None or value == "" or value == "None":
        return False
    return True

def add_product(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type:ignore
        return redirect("home")
    if  len(categories.get_all_category()) == 0 or len(brands.get_all_brand()) == 0:
        messages.error(request, "Please add category and brand first")
        return redirect("admin_products")
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Product added successfully")
            return redirect("admin_products")
    errors = form.errors
    return renderX(
        request,
        "admin/add.html",
        {
            "form": ProductForm(),
            "url": reverse("add_product"),
            "errors": errors,
        },
    )


def add_category(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type:ignore
        return redirect("home")
    form = CategoryForm()
    if request.method == "POST":
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Category added successfully")
            return redirect("admin_categories")
    errors = form.errors
    return renderX(
        request,
        "admin/add.html",
        {"form": CategoryForm(), "url": reverse("add_category"), "errors": errors},
    )


def add_brand(request: HtmxHttpRequest):
    if not request.user.is_superuser:  # type:ignore
        return redirect("/")
    form = BrandForm()
    if request.method == "POST":
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Brand added successfully")
            return redirect("admin_brands")
    errors = form.errors
    return renderX(
        request,
        "admin/add.html",
        {"form": BrandForm(), "url": reverse("add_brand"), "errors": errors},
    )

def add_address(request:HtmxHttpRequest):
    if request.user.is_authenticated:
        if request.POST:
            address = request.POST["address"]
            city = request.POST["city"]
            state = request.POST["state"]
            pincode = request.POST["pincode"]
            if check_none(address) and check_none(city) and check_none(state) and check_none(pincode):
                request.user.create_address(address=address, city=city, state=state, pincode=pincode) #type:ignore
                messages.success(request, "Address added successfully")
            else:messages.error(request, "Address cannot be added!")
            return redirect(request.META['HTTP_REFERER'])
        messages.error(request, "Address cannot be added!")
        return redirect(request.META['HTTP_REFERER'])
    return redirect("signin")