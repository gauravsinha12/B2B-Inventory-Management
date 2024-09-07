from django.shortcuts import redirect
from django.contrib import messages
from base.views.Htmx import HtmxHttpRequest, renderX
from base.models.productsModel import Products
from base.models.userModel import User
from base.forms import EnquiryForm, Enquiry
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

enquiries = Enquiry()
products = Products()
users = User()


def get_all_enquiries(request: HtmxHttpRequest):
    if request.user.is_superuser:# type:ignore
        return redirect("admin_products") 
    if request.user.is_authenticated:# type:ignore
        enquiryList = enquiries.get_enquiry_by_user(user=request.user)
        paginator = Paginator(enquiryList, 8)
        page = request.GET.get('page')
        try:
            enquiryList = paginator.page(page) #type:ignore
        except PageNotAnInteger:
            enquiryList = paginator.page(1) #type:ignore
        except EmptyPage:
            enquiryList = paginator.page(paginator.num_pages) #type:ignore
        return renderX(request, "allEnquiries.html", {"page": enquiryList,"end": paginator.num_pages})
    return redirect("signin")

def get_enquiry(request: HtmxHttpRequest,id):
    if not request.user.is_authenticated:
        return redirect("signin")
    enquiry = enquiries.get_enquiry_by_id(id=id)
    if request.user.is_superuser or request.user == enquiry.author: # type:ignore
        return renderX(request, "enquiry.html", {"enquiry": enquiry})
    return redirect("home")

def create_enquiry(request: HtmxHttpRequest):
    if request.method == "POST":
        form = EnquiryForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            product = products.get_product_by_id(id=request.POST["product"])
            author = request.user
            try:
                parent = form.cleaned_data["parent"]
            except:
                parent = None  
            enquiry = Enquiry(
                message=message,
                author=author,
                product=product,
                parent=parent,
            )
            enquiry.save()
            messages.success(request, f"{'Enquiry' if parent==None else 'Reply'} sent successfully")
            if parent:
                return redirect("get_enquiry", id=parent.id)
            return redirect("get_product", id=product.id) # type:ignore
    return redirect("signin")
