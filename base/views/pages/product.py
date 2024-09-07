from django.contrib import messages
from django.shortcuts import redirect
from base.forms import EnquiryForm
from base.models import Products
import random
from base.views.Htmx import HtmxHttpRequest, renderX

products = Products()
def get_product(request:HtmxHttpRequest,id):
    try:
        form = EnquiryForm()
        product = products.get_product_by_id(id=id)
        relatedCategory = list(products.filter_by_category(category=product.category.id)) #type:ignore
        relatedCategory = random.sample(relatedCategory,min(len(relatedCategory),5))
        relatedBrand = list(products.filter_by_category(category=product.brand.id)) #type:ignore
        random.sample(relatedBrand,min(5,len(relatedBrand)))
        if product.visibility == 0 and not request.user.is_superuser: # type: ignore
            messages.error(request,"No such Product.")
            return redirect("home")
        context={
            "product" : product,
            "enquiryForm":form,
            "relatedCategory":relatedCategory,
            "relatedBrand":relatedBrand
        }
        return renderX(request,"product.html",context)
    except:
        messages.error(request,"No such Product.")
        return redirect("home")