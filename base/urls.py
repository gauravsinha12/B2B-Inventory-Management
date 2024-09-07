from django.urls import path
from django.contrib.auth import views as auth_views
from base.views import *

base = [
    path("", home, name="home"),
    path("categories", all_categories, name="categories"),
    path("brands", all_brands, name="brands"),
    path("all-products", all_products, name="all_products"),
    path("search", search, name="search"),
    path("featured-products", featured_products, name="featured_products"),
    path("profile-page", profile_page, name="profile_page"),
    path("product/<int:id>", get_product, name="get_product"),
    path("category/<int:id>",get_category, name="get_category"),
    path("brand/<int:id>",get_brand, name="get_brand"),
    path("cart", cart, name="cart"),
    path("enquiries",get_all_enquiries,name="enquiries"),
    path("enquiry/<int:id>",get_enquiry,name="get_enquiry"),
    path("enquiry",create_enquiry,name="create_enquiry"),
    path("order", create_order, name="create_order"),
    path("orders", my_orders, name="my_orders"),
    path("previous-orders", previous_orders, name="previous_orders"),
    path("cancel-order", cancel_order, name="cancel_order"),
    path("checkout", checkout, name="checkout"),
    path("edit-address-form",edit_address_form,name="edit_address_form"),
    path("add-address-form",add_address_form,name="add_address_form"),
]

adminUrls = [
    path("admin/", admin_products, name="admin_products"),
    path("admin/categories", admin_categories, name="admin_categories"),
    path("admin/brands", admin_brands, name="admin_brands"),
    path("admin/users", admin_users, name="admin_users"),
    path("admin/orders", admin_orders, name="admin_orders"),
    path("admin/enquiries", admin_enquiries, name="admin_enquiries"),
    path("change-visibility", change_visibility, name="change_visibility"),
    path("change-featured", change_featured, name="change_featured"),
    path("change-active", change_user_active, name="change_user_active"),
    path("change-isbusiness", change_is_business, name="change_is_business"),
    path("change-order-status", change_order_status, name="change_order_status"),
    path("admin/add-product", add_product, name="add_product"),
    path("admin/add-category", add_category, name="add_category"),
    path("admin/add-brand", add_brand, name="add_brand"),
    path("admin/delete/product/",delete_product,name="delete_product"),
    path("admin/delete/order/",delete_order,name="delete_order"),
    path("admin/delete/enquiry/",delete_enquiry,name="delete_enquiry"),
    path("admin/delete/category/",delete_category,name="delete_category"),
    path("admin/delete/brand/",delete_brand,name="delete_brand"),
    path("admin/edit-product/<int:id>",edit_product,name="edit_product"),
    path("admin/edit-category/<int:id>",edit_category,name="edit_category"),
    path("admin/edit-brand/<int:id>",edit_brand,name="edit_brand"),
]

components = [
    path("add-address", add_address, name="add_address"),
    path("edit-address",edit_address,name="edit_address"),
    path("add-to-cart", add_to_cart, name="add_to_cart"),
    path("cart-count", cart_count, name="cart_count"),
    path(
        "field-edit",
        field_edit,
        name="field_edit",
    ),
    path(
        "field-update",
        field_update,
        name="field_update",
    ),
]

auth = [
    path("signup", user_signup, name="signup"),
    path("signin", user_login, name="signin"),
    path("signout", user_logout, name="signout"),
    path("changepassword", change_password, name="change_password"),
    path("changeprofilefrom", change_profile, name="change_profile_form"),
    path(
        "activate/<uid>/<token>",  # type: ignore
        user_activation,
        name="activate",
    ),
    path(
        "password_reset/",
        auth_views.PasswordResetView.as_view(
            template_name="auth/password_reset/form.html"
        ),
        name="password_reset",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="auth/password_reset/done.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="auth/password_reset/confirm.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset/done",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="auth/password_reset/complete.html"
        ),
        name="password_reset_complete",
    ),
]

urlpatterns = auth + base + components + adminUrls
