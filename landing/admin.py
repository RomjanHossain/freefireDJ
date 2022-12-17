from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (Buy, CarasolModel, ContactUs, Items, NewUser,
                     PaymentMethod, Services)


@admin.register(CarasolModel)
class CarasolModelAdmin(admin.ModelAdmin):
    list_display = (
        "carasol_title",
        "carasol_link",
        "carasol_image",
    )
    list_editable = ("carasol_link",)
    list_per_page = 10


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ("title", "poster")
    list_editable = ("poster",)
    list_per_page = 10


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ("price", "diamond")
    list_editable = ("price",)
    list_display_links = ("diamond",)
    list_per_page = 10


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ("name", "image", "account_id")
    list_editable = ("image", "account_id")
    list_per_page = 10


@admin.register(Buy)
class BuyAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "item",
        "date",
        "payment_method",
        "status",
        "sender_number",
        "trxId",
    )
    list_editable = ("status",)
    list_per_page = 10
    search_fields = ("user", "payment_method", "status", "sender_number", "trxId")


# @admin.register(NewUser)
# class NewUserAdmin(admin.ModelAdmin):
#     list_display = (
#         "username",
#         "phone",
#         "email",
#         "date_joined",
#     )
#     list_per_page = 10
#     search_fields = ("username", "email", "phone")


class UserAdminConfig(UserAdmin):
    model = NewUser
    search_fields = ("username", "email", "phone")
    list_filter = ("username", "email", "phone", "is_active", "is_staff")
    # ordering = ("-start_date",)
    list_display = (
        "username",
        "email",
        "phone",
    ) + UserAdmin.list_display

    fieldsets = (
        (None, {"fields": ("username", "email", "phone", "password")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser")}),
        ("Personal", {"fields": ("first_name", "last_name")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "email",
                    "phone",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(NewUser, UserAdminConfig)
admin.site.register(ContactUs)
