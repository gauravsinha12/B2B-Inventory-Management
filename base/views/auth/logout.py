from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    if not request.user.is_authenticated:return redirect('signin')
    messages.success(request,"Logged Out Successfully!")
    logout(request)
    return redirect('home')