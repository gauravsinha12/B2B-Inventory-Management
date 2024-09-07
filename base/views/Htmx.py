from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django_htmx.middleware import HtmxDetails
from base.templates.icons.avatars import avatars



class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails

def renderX(request: HtmxHttpRequest, template: str, context: dict) -> HttpResponse:
    base = "_partial.html" if request.htmx else "_base.html"
    context["base"] = base
    context["avatars"]=avatars
    if request.htmx:
        return render(request, template, context)
    else:
        return render(request, template, context)    