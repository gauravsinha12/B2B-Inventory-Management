from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from base.models.productsModel import Brand, Products
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

brands = Brand()
products = Products()


def all_brands(request: HtmxHttpRequest) -> HttpResponse:
    pList = products.get_all_products().values_list("brand")
    brandList = Brand.objects.filter(id__in=pList)
    brandList = brandList.order_by("-id")
    paginator = Paginator(brandList, 10)
    page = request.GET.get("page")
    try:
        brandList = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        brandList = paginator.page(1)
    except EmptyPage:
        brandList = paginator.page(paginator.num_pages)
    return renderX(
        request, "brands.html", {"page": brandList, "end": paginator.num_pages}
    )


def get_brand(request: HtmxHttpRequest, id):
    try:
        brand = brands.get_brand_by_id(id=id)
        filteredProducts = products.filter_by_brand(brand).filter(visibility=2)
        if not request.user.is_anonymous and request.user.is_business: #type:ignore
            filteredProducts = filteredProducts.union(products.filter_by_brand(brand).filter(visibility=1))
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
        messages.error(request, "Please select a brand")
        return redirect("brands")
