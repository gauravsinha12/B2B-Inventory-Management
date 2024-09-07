from django.contrib import messages
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import redirect
from base.forms import SignUpForm
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from base.views.Htmx import HtmxHttpRequest, renderX
from django.contrib.sites.shortcuts import get_current_site
from base.views.TokenGenerator import account_activation_token
from django_htmx.http import HttpResponseClientRedirect


def user_signup(request: HtmxHttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        form = SignUpForm()
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                user = form.save()
                current_site = get_current_site(request)
                mail_subject = "Activate your account."
                uid=urlsafe_base64_encode(force_bytes(user.pk))
                token = account_activation_token.make_token(user)
                message = render_to_string(
                    "auth/email_template.html",
                    {
                        "user": user,
                        "domain": current_site.domain,
                        "uid": uid,
                        "token": token,
                    },
                )
                to_email = form.cleaned_data.get("email")
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                messages.info(
                    request,
                    "Activation Link Was sent to email",
                )
                return HttpResponseClientRedirect("/signin")
        errors = form.errors
        return renderX(
            request,
            "auth/auth.html",
            {"form": SignUpForm(), "signUp": True, "errors": errors},
        )
    return redirect("/")
