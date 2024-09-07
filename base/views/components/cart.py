from base.views.Htmx import HtmxHttpRequest
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django_htmx.http import trigger_client_event
from base.models.userModel import User
from base.models.productsModel import Products

users = User()
products = Products()

def add_to_cart(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:redirect("signin")
    productInstance = products.get_product_by_id(id=int(request.POST["product"]))  # type: ignore
    cartInstance = request.user.get_cart_by_user_and_product(productInstance)  # type: ignore
    if not cartInstance:
        cartInstance = users.add_to_cart(productInstance,ib=request.user.is_business) # type: ignore 
        request.user.cart.add(cartInstance)# type: ignore
    else:
        q=cartInstance.quantity
        if request.POST['action'] == 'add':
            q+=1
        elif request.POST['action'] == 'remove':
            q-=1
        cartInstance = request.user.update_cart(cartInstance,max(q,0))  # type: ignore
    page = "partials/cart/addToCart.html" if cartInstance.quantity==0 else "partials/cart/addToCartActive.html"  # type: ignore
    cart = cartInstance if cartInstance.quantity > 0 else cartInstance.product
    response = render(request, page, {"cart": cart})
    trigger_client_event(response,'updateCartCount',{})
    return response

def cart_count(request: HtmxHttpRequest) -> HttpResponse:
    if request.user.is_anonymous:
        return HttpResponse()
    count=0
    for cart in request.user.cart.all(): # type: ignore
        count+=cart.quantity
    return render(request,"icons/badge.html",{"count":count})