from django.http import HttpResponse
from django.shortcuts import redirect
from base.models import Enquiry, User, Category, Brand, Products,Order
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

enquiry = Enquiry()
users = User()
products = Products()
categories = Category()
brands = Brand()
orders = Order()

def admin_products(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser: # type: ignore
        return redirect("home")  
    category = request.POST.get("category")
    brand = request.POST.get("brand")
    if category:
        filteredProducts = products.filter_by_category(category)
    elif brand:
        filteredProducts = products.filter_by_brand(brand)
    else:
        filteredProducts = products.get_all_products()
    filteredProducts = filteredProducts.order_by("-id")
    paginator = Paginator(filteredProducts, 8)
    page = request.GET.get("page")
    try:
        filteredProducts = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        filteredProducts = paginator.page(1)
    except EmptyPage:
        filteredProducts = paginator.page(paginator.num_pages)
    context = {
        "nav":0,
        "products": filteredProducts,
        "categories": reversed(categories.get_all_category()),
        "brands": reversed(brands.get_all_brand()),
        "selectedCategory": int(category if category else 0),
        "selectedBrand": int(brand if brand else 0),
        "end": paginator.num_pages,
        "h":"h-4/5"
    }
    return renderX(request, "admin/products.html", context)


def admin_categories(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    filteredCategories = categories.get_all_category()
    filteredCategories = filteredCategories.order_by("-id")
    paginator = Paginator(filteredCategories, 8)
    page = request.GET.get("page")
    try:
        filteredCategories = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        filteredCategories = paginator.page(1)
    except EmptyPage:
        filteredCategories = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "admin/categories.html",
        {
            "nav":1,
            "categories": filteredCategories,
            "end": paginator.num_pages,
        },
    )


def admin_enquiries(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    filteredEnquiries = enquiry.get_all_enquiry()
    filteredEnquiries = filteredEnquiries.order_by("-id")
    paginator = Paginator(filteredEnquiries, 8)
    page = request.GET.get("page")
    try:
        filteredEnquiries = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        filteredEnquiries = paginator.page(1)
    except EmptyPage:
        filteredEnquiries = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "admin/enquiries.html",
        {
            "enquiries": filteredEnquiries,
            "end": paginator.num_pages,
        },
    )


def admin_orders(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type:ignore
        return redirect("home")
    orderList = orders.get_all_order_by_filters()
    orderList = orderList.order_by("-id")
    paginator = Paginator(orderList, 8)
    page = request.GET.get("page")
    try:
        orderList = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        orderList = paginator.page(1)
    except EmptyPage:
        orderList = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "admin/orders.html",
        {
            "orders": orderList,
            "end": paginator.num_pages,
        },
    )


def admin_brands(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    filteredBrands = brands.get_all_brand()
    filteredBrands = filteredBrands.order_by("-id")
    paginator = Paginator(filteredBrands, 8)
    page = request.GET.get("page")
    try:
        filteredBrands = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        filteredBrands = paginator.page(1)
    except EmptyPage:
        filteredBrands = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "admin/brands.html",
        {
            "nav":2,
            "brands": filteredBrands,
            "end": paginator.num_pages,
        },
    )


def admin_users(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_superuser:  # type: ignore
        return redirect("home")
    usersList = users.get_all_users()
    usersList = usersList.order_by("-id")
    paginator = Paginator(usersList, 8)
    page = request.GET.get("page")
    try:
        usersList = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        usersList = paginator.page(1)
    except EmptyPage:
        usersList = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "admin/users.html",
        {
            "users": usersList,
            "end": paginator.num_pages,
        },
    )
