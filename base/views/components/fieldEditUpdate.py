from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from base.views.Htmx import HtmxHttpRequest, renderX
from base.models.userModel import User
from base.models.productsModel import Products

users = User()
products = Products()


def field_edit(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_authenticated: return redirect("signin") #type:ignore
    try:
        field = request.POST["field"]
        fieldName = request.POST["fieldName"]
        product = request.POST["product"]
        user = request.POST["user"]
        return renderX(
            request,
            "partials/admin/fieldUpdate.html",
            {
                "field": field,
                "fieldName": fieldName,
                "product": product,
                "user": user if user != None else "",
            },
        )
    except:
        return renderX(
            request, "partials/admin/fieldEdit.html", {"field": "Invalid Input"}
        )


def field_update(request: HtmxHttpRequest) -> HttpResponse: #type:ignore
    if not request.user.is_authenticated: return redirect("signin") #type:ignore
    fieldName = request.POST["fieldName"]
    try:
        field = round(float(request.POST["field"]))
        user = users.get_user_by_email(request.POST["user"])
        product = None
        if fieldName == "userDiscount":
            user.additional_discount = max(0, min(field, 99))  # type:ignore
            user.save()
        elif fieldName == "productPrice":
            product = products.get_product_by_id(request.POST["product"])
            product.price = max(field, 0)
            product.save()
        elif fieldName == "productBusinessPrice":
            product = products.get_product_by_id(request.POST["product"])
            product.businessPrice = max(field, 0)
            product.save()
        elif fieldName == "productDiscount":
            product = products.get_product_by_id(request.POST["product"])
            product.discount = max(0, min(field, 99))  # type:ignore
            product.save()
        elif fieldName == "productInventory":
            product = products.get_product_by_id(request.POST["product"])
            product.inventory = max(field, 0)
            product.save()
        elif fieldName == "productPackOf":
            product = products.get_product_by_id(request.POST["product"])
            product.packOf = max(field,0)
            product.save()
        elif fieldName == "productInCase":
            product = products.get_product_by_id(request.POST["product"])
            product.inCase = max(field,0)
            product.save()
        elif fieldName == "cartQuantity":
            cartItem = user.get_cart_by_user_and_product(  # type:ignore
                products.get_product_by_id(request.POST["product"])
            ) 
            user.update_cart(cartItem,max(field,0))

        if "product" in fieldName:
            messages.success(request,"Successfully updated Product")
            return redirect("admin_products")
        elif "user" in fieldName:
            messages.success(request,"Successfully updated User")
            return redirect("admin_users")
        elif "cart" in fieldName:
            messages.success(request,"Updated Cart")
            return redirect("cart")
            
    except Exception as e:
        if "product" in fieldName:
            messages.error(request,"Invalid Value")
            return redirect("admin_products")
        elif "user" in fieldName:
            messages.error(request,"Invalid Value")
            return redirect("admin_users")
        elif "cart" in fieldName:
            messages.error(request,"Invalid Value")
            return redirect("cart")