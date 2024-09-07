from django.http import HttpResponse
from base.models import User
from base.views.Htmx import HtmxHttpRequest, renderX

def profile_page(request: HtmxHttpRequest) -> HttpResponse:
    user = request.user
    context = {
        'user': user,
    }
    return renderX(request, 'profile.html', context)