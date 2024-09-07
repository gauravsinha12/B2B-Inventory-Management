from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from base.views.Htmx import HtmxHttpRequest, renderX
from django_htmx.http import trigger_client_event, push_url
from base.models.orderModel import Order
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

orders = Order()


def my_orders(request: HtmxHttpRequest):
    if request.user.is_superuser:  # type:ignore
        return redirect("admin_orders")
    if request.user.is_authenticated:
        userOrder = orders.get_all_order_by_filters(
            status=[1, 2, 3], user=request.user
        ).reverse()
        paginator = Paginator(userOrder, 6)
        page = request.GET.get("page")
        try:
            userOrder = paginator.page(page)  # type:ignore
        except PageNotAnInteger:
            userOrder = paginator.page(1)
        except EmptyPage:
            userOrder = paginator.page(paginator.num_pages)
        return renderX(
            request,
            "orders.html",
            {
                "page": userOrder,
                "previous": False,
                "end": paginator.num_pages,
            },
        )
    return redirect("signin")


def previous_orders(request: HtmxHttpRequest):
    if request.user.is_superuser:  # type:ignore
        return redirect("admin_orders")
    if request.user.is_authenticated:
        userOrder = orders.get_all_order_by_filters(
            status=[4, 5], user=request.user
        ).reverse()
        paginator = Paginator(userOrder, 6)
        page = request.GET.get("page")
        try:
            userOrder = paginator.page(page)  # type:ignore
        except PageNotAnInteger:
            userOrder = paginator.page(1)
        except EmptyPage:
            userOrder = paginator.page(paginator.num_pages)
        return renderX(
            request,
            "orders.html",
            {
                "page": userOrder,
                "previous": True,
                "end": paginator.num_pages,
            },
        )
    return redirect("signin")


# create order
def create_order(request: HtmxHttpRequest):
    if request.user.is_superuser:  # type:ignore
        return redirect("admin_orders")
    if request.user.is_authenticated:
        try:
            selected = int(request.POST["address"])
            items = request.user.cart.filter(quantity__gt=0)  # type:ignore
            for item in items:
                orders.create_order(  # type:ignore
                    address=request.user.addresses.get(id=selected),  # type:ignore
                    user=request.user,
                    status=1,
                    item=item,
                )
                item.product.inventory -= item.quantity
                item.product.save()
            items.delete()  # type:ignore
            messages.success(request, "Order created successfully")
            userOrder = orders.get_all_order_by_filters(
                status=[1, 2, 3], user=request.user
            ).reverse()
            paginator = Paginator(userOrder, 6)
            page = request.GET.get("page")
            try:
                userOrder = paginator.page(page)  # type:ignore
            except PageNotAnInteger:
                userOrder = paginator.page(1)
            except EmptyPage:
                userOrder = paginator.page(paginator.num_pages)
            response = renderX(
                request,
                "orders.html",
                {
                    "page": userOrder,
                    "previous": False,
                    "end": paginator.num_pages,
                },
            )
            trigger_client_event(response, "updateCartCount", {})
            push_url(response, reverse("my_orders"))
            return response
        except:
            messages.error(request, "Please select an address")
            return redirect("checkout")
    return redirect("signin")


def cancel_order(request: HtmxHttpRequest):
    if request.user.is_authenticated:
        try:
            orders.cancel_an_order(int(request.POST["order_id"]))  # type:ignore
            messages.success(request, "Order cancelled successfully")
        except:
            messages.error(request, "No Such Order")
        return redirect("my_orders")
    return redirect("signin")
