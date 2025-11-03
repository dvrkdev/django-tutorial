from django.contrib import admin
from .models import Reservation, Item


class ReservationAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "guest_count",
        "reservation_time",
        "comments",
    ]


admin.site.register(Reservation, ReservationAdmin)


class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price"]


admin.site.register(Item, ItemAdmin)
