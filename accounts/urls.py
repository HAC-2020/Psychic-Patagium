from django.urls import include, path

from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup/", views.signup_page, name="signup"),
    path("accounts/profile/", views.profile, name="profile"),
    path(
        "accounts/signup/customer/",
        views.CustomerSignUpView.as_view(),
        name="customer_signup",
    ),
    path(
        "accounts/signup/shopowner/",
        views.ShopOwnerSignUpView.as_view(),
        name="shopowner_signup",
    ),
]
