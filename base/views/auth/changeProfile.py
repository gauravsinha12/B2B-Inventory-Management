from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import redirect
from base.forms import ChangeUserProfileForm
from base.views.Htmx import renderX

def change_profile(request):
    if not request.user.is_authenticated:return redirect('signin')
    form = ChangeUserProfileForm(instance=request.user)
    if request.method == "POST":
        form = ChangeUserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your Profile was successfully updated!")
            return redirect("profile_page")
    errors = form.errors
    form = ChangeUserProfileForm(instance=request.user)
    form.order_fields(
        field_order=[
            "email",
            "first_name",
            "last_name",
        ]
    )
    return renderX(
        request,
        "auth/changeprof.html",
        {"form": form,"errors": errors,},
    )
