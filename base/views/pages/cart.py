from base.views.Htmx import renderX
from django_htmx.http import trigger_client_event
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def cart(request):
    if not request.user.is_authenticated:
        return renderX(
            request,
            "cart.html",
            {
                "cart": [],
            },
        )
    cartList = request.user.cart.all()
    paginator = Paginator(cartList, 8)
    page = request.GET.get("page")
    try:
        cartList = paginator.page(page)  # type:ignore
    except PageNotAnInteger:
        cartList = paginator.page(1)
    except EmptyPage:
        cartList = paginator.page(paginator.num_pages)
    response = renderX(
        request,
        "cart.html",
        {"page": cartList, "end": paginator.num_pages, "cart": request.user.cart.all()},
    )
    trigger_client_event(response, "updateCartCount", {})
    return response
