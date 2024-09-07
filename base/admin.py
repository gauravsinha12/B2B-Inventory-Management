from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from base.models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email','first_name','last_name','date_joined','password','addresses')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser',"is_business")}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active','is_superuser')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
admin.site.register(User, CustomUserAdmin)

admin.site.register(Products)
admin.site.register(Address)
admin.site.register(Enquiry)
admin.site.register(Order)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(CartItem)