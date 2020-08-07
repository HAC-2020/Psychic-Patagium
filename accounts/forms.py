from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User


class CustomerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "date_of_birth",
            "mobile_no",
        ]

    def save(self):
        user = super().save(commit=False)
        user.is_customer = True
        user.save()
        return user


class ShopOwnerSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
            "date_of_birth",
            "mobile_no",
        ]

    def save(self):
        user = super().save(commit=False)
        user.is_shopowner = True
        user.save()
        return user
