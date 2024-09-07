from django.contrib import messages
from django.shortcuts import redirect
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from base.views.TokenGenerator import account_activation_token
from base.models.userModel import User
from django.contrib.auth import login

def user_activation(request, uid, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist) as e:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, "Account Activated")
        return redirect("/signin")
    messages.error(request, "Activation link is invalid!")
    return redirect("/signup")