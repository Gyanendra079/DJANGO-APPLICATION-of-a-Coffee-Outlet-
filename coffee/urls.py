from django.urls import path

from . import views

urlpatterns = [

# --------------------------------------------------------
# HOME
# --------------------------------------------------------

path(
    "",
    views.home,
    name="home"
),


# --------------------------------------------------------
# MENU
# --------------------------------------------------------

path(
    "menu/",
    views.menu,
    name="menu"
),


# --------------------------------------------------------
# CHECKOUT
# --------------------------------------------------------

path(
    "order/",
    views.order,
    name="order"
),


# --------------------------------------------------------
# ORDER CONFIRMATION
# --------------------------------------------------------

path(
    "order/confirmation/<int:order_id>/",
    views.order_confirmation,
    name="order_confirmation"
),


# --------------------------------------------------------
# TRACK ORDER
# --------------------------------------------------------

path(
    "track-order/",
    views.track_order,
    name="track_order"
),


# --------------------------------------------------------
# CONTACT
# --------------------------------------------------------

path(
    "contact/",
    views.contact,
    name="contact"
),


# --------------------------------------------------------
# CART
# --------------------------------------------------------

path(
    "cart/",
    views.cart,
    name="cart"
),


# --------------------------------------------------------
# ADD TO CART
# --------------------------------------------------------

path(
    "cart/add/<int:product_id>/",
    views.add_to_cart,
    name="add_to_cart"
),


# --------------------------------------------------------
# INCREASE QUANTITY
# --------------------------------------------------------

path(
    "cart/increase/<int:product_id>/",
    views.increase_quantity,
    name="increase_quantity"
),


# --------------------------------------------------------
# DECREASE QUANTITY
# --------------------------------------------------------

path(
    "cart/decrease/<int:product_id>/",
    views.decrease_quantity,
    name="decrease_quantity"
),


# --------------------------------------------------------
# REMOVE FROM CART
# --------------------------------------------------------

path(
    "cart/remove/<int:product_id>/",
    views.remove_from_cart,
    name="remove_from_cart"
),


]
