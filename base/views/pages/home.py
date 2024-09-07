from django.http import HttpResponse
from base.models.productsModel import Products
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

products = Products()
def home(request: HtmxHttpRequest) -> HttpResponse:
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
    return renderX(request, "home.html", {"page": productList,"end": paginator.num_pages})