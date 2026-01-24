from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ["username", "email", "location", "is_staff"]
    fieldsets = UserAdmin.fieldsets + (
        (
            "Social Links & Info",
            {
                "fields": (
                    "location",
                    "bio",
                    "github_link",
                    "linkedin_link",
                    "x_link",
                    "website_link",
                )
            },
        ),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            "Social Links & Info",
            {
                "fields": (
                    "location",
                    "bio",
                    "github_link",
                    "linkedin_link",
                    "x_link",
                    "website_link",
                )
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
