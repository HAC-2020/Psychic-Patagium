from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from .forms import CustomerSignUpForm, ShopOwnerSignUpForm
from .models import User


def signup_page(request):
    return render(request, "registration/signup.html")


@login_required
def profile(request):
    return render(request, "registration/profile.html")


class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = "registration/signup_form.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("location_select")


class ShopOwnerSignUpView(CreateView):
    model = User
    form_class = ShopOwnerSignUpForm
    template_name = "registration/signup_form.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("shop_select")
