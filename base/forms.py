from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    UsernameField,
    PasswordChangeForm,
    UserChangeForm,
)
from base.models import Products,User,Enquiry,Address,Category,Brand
from localflavor.in_.forms import INZipCodeField, INStateSelect
from cloudinary.forms import CloudinaryFileField

INPUTDECORATOR = "outline-none focus:outline-none focus:ring-0"


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label="Enter Password",
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
        help_text="""
            <ul class="list-disc list-inside mb-2 text-xs">
                <li>Your password can't be too similar to your other personal information.</li>
                <li>Your password must contain at least 8 characters.</li>
                <li>Your password can't be a commonly used password.</li>
                <li>Your password can't be entirely numeric.</li>
            </ul>
            """,
    )
    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
         help_text="""
            <ul class="list-disc list-inside mb-2 text-xs">
                <li>Enter the same password as before, for verification.</li>
            </ul>
            """,
    )

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "phone"]
        labels = {
            "email": "Enter Email",
            "first_name": "Enter First Name",
            "last_name": "Enter Last Name",
            "phone": "Enter Phone Number",
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR, "type": "tel"}
            ),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(
        label="Enter Email",
        widget=forms.TextInput(
            attrs={"autofocus": True, "placeholder": "", "class": INPUTDECORATOR}
        ),
    )
    password = forms.CharField(
        label="Enter Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
    )


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(
        label="Old Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
    )
    new_password1 = forms.CharField(
        label="New Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
    )
    new_password2 = forms.CharField(
        label="Confirm Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
    )


class ChangeUserProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = {"email", "first_name", "last_name", "phone"}
        labels = {
            "email": "Email",
            "first_name": "First Name",
            "last_name": "Last Name",
            "phone": "Phone Number",
        }
        widgets = {
            "email": forms.EmailInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "first_name": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "last_name": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "phone": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR, "type": "tel"}
            ),
        }


class AdminUserChangeForm(UserChangeForm):
    password = forms.PasswordInput(attrs={"type": "hidden"})
    usergroup = forms.ModelChoiceField(
        Group.objects.all(), label="User Permission Level", empty_label=None
    )

    class Meta:
        model = User
        fields = {"is_superuser", "is_active", "is_staff", "usergroup"}
        labels = {
            "is_superuser": "Set Admin",
            "is_active": "Set Active",
            "is_staff": "Make Staff Member",
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ["parent", "message"]
        labels = {"message": "Message"}
        widgets = {
            "message": forms.Textarea(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
        }


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ["address", "city", "state", "pincode"]
        labels = {
            "address": "Address",
            "city": "City",
            "state": "State",
            "pincode": "Pincode",
        }
        widget = {
            "address": forms.TextInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "city": forms.TextInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
            "state": forms.ChoiceField(widget=INStateSelect(), initial="DL"),
            "pincode": INZipCodeField(),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = [
            "name",
            "description",
            "price",
            "businessPrice",
            "discount",
            "inventory",
            "packOf",
            "inCase",
            "image1",
            "image2",
            "image3",
            "image4",
            "video",
            "category",
            "brand",
            "visibility",
        ]
        labels = {
            "name": "Product Name",
            "description": "Description",
            "price": "Price",
            "businessPrice": "Business Price",
            "discount": "Discount",
            "inventory": "Inventory",
            "packOf": "Pack Contains",
            "inCase": "Case Contains",
            "image1": "",
            "image2": "",
            "image3": "",
            "image4": "",
            "video": "Video",
            "category": "Category",
            "brand": "Brand",
            "visibility": "Visibility",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
            "description": forms.Textarea(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "price": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "businessPrice": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "discount": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR,"max":"99","min":"0"}
            ),
            "inventory": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "packOf": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "inCase": forms.NumberInput(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
            "video": forms.URLInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
            "category": forms.Select(attrs={"class": INPUTDECORATOR}),
            "brand": forms.Select(attrs={"class": INPUTDECORATOR}),
            "visibility": forms.Select(attrs={"class": INPUTDECORATOR}),
        }

    image1 = CloudinaryFileField(
        options={
                "tags": "fireworks",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
        },
    ),

    image2 = CloudinaryFileField(
        options={
                "tags": "fireworks",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
            },
    ),

    image3 = CloudinaryFileField(
        options={
                "tags": "fireworks",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
            },
    ),

    image4 = CloudinaryFileField(
        options={
                "tags": "fireworks",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
            },
    ),

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description","image"]
        labels = {
            "name": "Category Name",
            "description": "Description",
            "image":"Image"
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
            "description": forms.Textarea(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
        }
    image = CloudinaryFileField(
        options={
                "tags": "category",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
        },
    ),

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ["name", "description","image"]
        labels = {
            "name": "Brand Name",
            "description": "Description",
            "image":"Image"
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "", "class": INPUTDECORATOR}),
            "description": forms.Textarea(
                attrs={"placeholder": "", "class": INPUTDECORATOR}
            ),
        }
    image = CloudinaryFileField(
        options={
                "tags": "brands",
                "crop": "limit",
                "width": 1000,
                "height": 1000,
                "eager": [{"crop": "fill", "width": 150, "height": 100}],
        },
    ),