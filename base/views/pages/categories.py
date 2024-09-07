from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from base.models.productsModel import Category, Products
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

categories = Category()
products = Products()


def all_categories(request: HtmxHttpRequest) -> HttpResponse:
    pList = products.get_all_products().values_list("category")
    categoryList = Category.objects.filter(id__in=pList)
    categoryList = categoryList.order_by("-id")
    paginator = Paginator(categoryList, 10)
    page = request.GET.get("page")
    try:
        categoryList = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        categoryList = paginator.page(1)
    except EmptyPage:
        categoryList = paginator.page(paginator.num_pages)
    return renderX(
        request,
        "categories.html",
        {
            "page": categoryList,
            "end": paginator.num_pages,
        },
    )


def get_category(request: HtmxHttpRequest, id):
    try:
        category = Category().get_category_by_id(id=id)
        filteredProducts = products.filter_by_category(category).filter(visibility=2)
        if not request.user.is_anonymous and request.user.is_business: #type:ignore
            filteredProducts = filteredProducts.union(products.filter_by_category(category).filter(visibility=1))
        filteredProducts = filteredProducts.order_by("-id")
        paginator = Paginator(filteredProducts, 8)
        page = request.GET.get("page")
        try:
            filteredProducts = paginator.page(page)  # type:ignore
        except PageNotAnInteger:
            filteredProducts = paginator.page(1)  # type:ignore
        except EmptyPage:
            filteredProducts = paginator.page(paginator.num_pages)
        return renderX(
            request,
            "home.html",
            {
                "page": filteredProducts,
                "end": paginator.num_pages,
            },
        )
    except:
        messages.error(request, "Please select a Category")
        return redirect("categories")
