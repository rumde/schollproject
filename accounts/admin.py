from django.contrib import admin
from .models import User, Department
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from simple_history.admin import SimpleHistoryAdmin

# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # list_display = ["address", "user", "country"]
    list_display = [
        "email", 
        "get_full_name",
        "user_type",
        "is_staff", "is_active",
        # "is_email_verified"
        "updated"
    ]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "dob")}),
        ("User Profile", {
            "classes": ("wide",),
            # "is_email_verified")
            "fields": ("image", "user_type", "country", "city", "department",)
        }),
        ("Permissions", {"fields": 
            ("is_superuser",
            
            "is_staff", "is_active", "user_permissions", "groups")
        }
        ),
        ("Important dates", {
            "fields": (
                "last_login",
                # "date_joined", "updated"
                )
            }
        ),
    )
    search_fields = ("email", "first_name", "last_name")


@admin.register(Department)
class DepartmentAdmin(SimpleHistoryAdmin):
    list_display = (
        "uid",
        "title",
        "sub_title",
        "state",
        "status",
        "timestamp",
        "updated",
    )
    list_filter = ("status", "timestamp", "updated", )
    readonly_fields = ("uid",)
