from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import redirect
from django_htmx.http import HttpResponseClientRedirect
from base.forms import LoginForm
from base.views.Htmx import HtmxHttpRequest, renderX
from django.contrib.auth import authenticate, login


def user_login(request: HtmxHttpRequest) -> HttpResponse:  # type: ignore
    if not request.user.is_authenticated:
        form = LoginForm()
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                email = form.cleaned_data["username"]
                upass = form.cleaned_data["password"]
                user = authenticate(username=email, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged in Successfully")
                    return HttpResponseClientRedirect("/")
        errors = form.errors
        return renderX(
            request,
            "auth/auth.html",
            {"form": LoginForm(), "signUp": False, "errors": errors},
        )
    return redirect("home")
