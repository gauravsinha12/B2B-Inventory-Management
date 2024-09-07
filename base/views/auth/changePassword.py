from django.shortcuts import redirect
from base.forms import ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from base.views.Htmx import renderX


def change_password(request):
    if not request.user.is_authenticated:return redirect('signin')
    form = ChangePasswordForm(request.user)
    if request.method == "POST":
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, "Your password was successfully updated!")
            return redirect("/")    
    errors = form.errors
    return renderX(
        request,
        "auth/changepass.html",
        {"form": ChangePasswordForm(request.user), "errors": errors},
    )
