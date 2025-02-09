from django import forms
from facility_mgn.widgets import ImageWidget
from django.contrib.auth.forms import UserCreationForm
from .models import User

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        # exclude = (
        #     "user_type", "date_joined",
        #     "is_superuser", "is_staff", "is_active", 
        #     "last_login", "groups", "user_permissions"
        # )
        fields = (
            "email",
            "first_name",
            "other_name",
            "last_name",
            "gender",
            "phone_number",
            "image",
            "dob",
            "country",
            "state",
            "city",
            "department",
        )

