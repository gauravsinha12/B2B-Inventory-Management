from django.shortcuts import redirect
from django.urls import reverse
from base.forms import AddressForm
from base.views.Htmx import HtmxHttpRequest, renderX
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def checkout(request: HtmxHttpRequest):
    if request.user.is_authenticated:
        cartList = request.user.cart.all()  # type:ignore
        paginator = Paginator(cartList, 8)
        page = request.GET.get("page")
        try:
            cartList = paginator.page(page)  # type:ignore
        except PageNotAnInteger:
            cartList = paginator.page(1)  # type:ignore
        except EmptyPage:
            cartList = paginator.page(paginator.num_pages)  # type:ignore
        return renderX(
            request,
            "checkout.html",
            {
                "cart": request.user.cart.all,  # type:ignore
                "addressForm": AddressForm(),
                "page": cartList,
                "end": paginator.num_pages,
            },
        )
    return redirect("signin")


def add_address_form(request: HtmxHttpRequest):
    if request.user.is_authenticated:
        return renderX(
            request,
            "partials/addAddressForm.html",
            {"addressForm": AddressForm(), "title": "Edit Address","url":request.META["HTTP_REFERER"]},
        )
    return redirect("signin")


def edit_address_form(request: HtmxHttpRequest):
    if request.user.is_authenticated:
        address_id = request.POST["address_id"]
        address = request.user.addresses.get(id=address_id)  # type:ignore
        form = AddressForm(instance=address)
        return renderX(
            request,
            "partials/addAddressForm.html",
            {
                "addressForm": form,
                "action": reverse("edit_address"),
                "addressId": address_id,
                "title": "Edit Address",
                "url":request.META["HTTP_REFERER"]
            },
        )
    return redirect("signin")
