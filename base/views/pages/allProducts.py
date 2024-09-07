from django.http import HttpResponse
from django.shortcuts import redirect
from base.models.productsModel import Products
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

products = Products()
def all_products(request: HtmxHttpRequest) -> HttpResponse:
    if  not request.user.is_authenticated or not request.user.is_business: return redirect("home") #type:ignore
    if request.user.is_superuser:return redirect("admin_products") #type:ignore
    productList=products.filter_by_visibility(2)
    if not request.user.is_anonymous and request.user.is_business: #type:ignore
        productList=productList.union(products.filter_by_visibility(1))
    productList = productList.order_by("-id")
    paginator = Paginator(productList, 8)
    page = request.GET.get('page')
    try:
        productList = paginator.page(page) #type:ignore
    except PageNotAnInteger:
        productList = paginator.page(1) #type:ignore
    except EmptyPage:
        productList = paginator.page(paginator.num_pages) #type:ignore
    context = {
        "products": productList,
        "end": paginator.num_pages,
        "h":"h-4/5"
        
    }
    return renderX(request, "allProducts.html", context)