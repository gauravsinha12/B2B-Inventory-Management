from django.http import HttpResponse
from base.models import Products
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def search(request: HtmxHttpRequest) -> HttpResponse:
    query = request.GET.get("search")
    if query:
        productList = Products.objects.filter(name__icontains=query)
    else:
        productList = Products.objects.all()
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
