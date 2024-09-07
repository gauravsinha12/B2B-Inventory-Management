from django import template
from base.models.userModel import User
from localflavor.in_.in_states import STATE_CHOICES
register = template.Library()

@register.simple_tag()
def discount(price=0,discount=0,userDiscount=0,*args, **kwargs):
    discounted = round(int(price) - int(price) * int(discount) / 100)
    return round(int(discounted) - int(discounted) * int(userDiscount) / 100)

@register.simple_tag()
def inflate(price,discount,userDiscount,*args,**kwargs):
    discounted = round(int(price) + int(price) * int(discount) / 100)
    return round(int(discounted) - int(discounted) * int(userDiscount) / 100)

@register.simple_tag()
def cart(user,procuct,*args,**kwargs):
    return User.get_cart_by_user_and_product(user,procuct)

@register.simple_tag()
def cart_count(cart,*args,**kwargs):
    quantity=0
    for item in cart:
        quantity+=item.quantity
    return quantity

@register.simple_tag()
def media_count(product,*args,**kwargs):
    length=1
    if product.image2:length+=1
    if product.image3:length+=1
    if product.image4:length+=1
    if product.video:length+=1
    return [i+1 for i in range(length)]

@register.simple_tag()
def cart_total(cart,*args,**kwargs):
    total=0
    for item in cart:
        total+=item.totalPrice
    return total

@register.simple_tag()
def cart_total_discount(cart,*args,**kwargs):
    total=0
    for item in cart:
        total+=item.discountedPrice
    return total

@register.simple_tag()
def state_name(state,*args,**kwargs):
    for i in STATE_CHOICES:
        if i[0]==state:
            return i[1]
    return None

@register.simple_tag()
def get_name(url,*args,**kwargs):
    return f"{url.split('-')[0].split('/')[-1].capitalize()} {url.split('-')[1].capitalize().split('/')[0]}"