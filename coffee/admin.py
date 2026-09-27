from django.contrib import admin

from .models import MenuItem, Order, OrderItem


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "is_available",
        "created_at",
    )

    list_filter = (
        "category",
        "is_available",
    )

    search_fields = (
        "name",
        "description",
    )

    ordering = (
        "-created_at",
    )


class OrderItemInline(admin.TabularInline):

    model = OrderItem

    extra = 0

    readonly_fields = (
        "price",
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "customer_name",
        "phone",
        "total_amount",
        "status",
        "created_at",
    )

    list_filter = (
        "status",
        "created_at",
    )

    search_fields = (
        "customer_name",
        "phone",
        "email",
    )

    readonly_fields = (
        "created_at",
        "total_amount",
    )

    inlines = [
        OrderItemInline
    ]

    ordering = (
        "-created_at",
    )


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):

    list_display = (
        "order",
        "menu_item",
        "quantity",
        "price",
    )

    list_filter = (
        "menu_item",
    )