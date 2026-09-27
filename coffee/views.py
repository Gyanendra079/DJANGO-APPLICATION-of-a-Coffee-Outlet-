from decimal import Decimal

from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CheckoutForm, OrderTrackingForm
from .models import MenuItem, Order, OrderItem


# Home page
def home(request):
    return render(request, "coffee/home.html")


# Menu page
def menu(request):
    menu_items = MenuItem.objects.filter(is_available=True)

    return render(
        request,
        "coffee/menu.html",
        {
            "menu_items": menu_items
        }
    )


# Checkout / Place Order
def order(request):
    cart = request.session.get("cart", {})

    # Do not allow checkout with an empty cart
    if not cart:
        return redirect("cart")

    cart_items = []
    total = Decimal("0.00")

    # Get products from the cart
    for product_id, quantity in cart.items():

        product = get_object_or_404(
            MenuItem,
            id=product_id,
            is_available=True
        )

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    # Customer submitted the checkout form
    if request.method == "POST":

        form = CheckoutForm(request.POST)

        if form.is_valid():

            # Create Order and OrderItems together
            with transaction.atomic():

                new_order = Order.objects.create(
                    customer_name=form.cleaned_data["customer_name"],
                    phone=form.cleaned_data["phone"],
                    email=form.cleaned_data["email"],
                    address=form.cleaned_data["address"],
                    total_amount=total,
                    status="Received",
                )

                # Create OrderItem for every cart product
                for item in cart_items:

                    OrderItem.objects.create(
                        order=new_order,
                        menu_item=item["product"],
                        quantity=item["quantity"],
                        price=item["product"].price,
                    )

            # Empty the cart after successful order
            request.session["cart"] = {}
            request.session.modified = True

            # Go to order confirmation page
            return redirect(
                "order_confirmation",
                order_id=new_order.id
            )

    else:
        # Display empty checkout form
        form = CheckoutForm()

    return render(
        request,
        "coffee/order.html",
        {
            "form": form,
            "cart_items": cart_items,
            "total": total,
        }
    )


# Order confirmation page
def order_confirmation(request, order_id):
    order = get_object_or_404(
        Order,
        id=order_id
    )

    return render(
        request,
        "coffee/order_confirmation.html",
        {
            "order": order
        }
    )


# Track an existing order
def track_order(request):
    order = None

    if request.method == "POST":

        form = OrderTrackingForm(request.POST)

        if form.is_valid():

            order_id = form.cleaned_data["order_id"]
            phone = form.cleaned_data["phone"]

            try:

                order = Order.objects.get(
                    id=order_id,
                    phone=phone
                )

            except Order.DoesNotExist:

                form.add_error(
                    None,
                    "Order not found. Please check your Order ID and phone number."
                )

    else:
        form = OrderTrackingForm()

    return render(
        request,
        "coffee/track_order.html",
        {
            "form": form,
            "order": order,
        }
    )


# Contact page
def contact(request):
    return render(
        request,
        "coffee/contact.html"
    )


# Add product to cart
def add_to_cart(request, product_id):

    product = get_object_or_404(
        MenuItem,
        id=product_id,
        is_available=True
    )

    cart = request.session.get(
        "cart",
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1
    else:
        cart[product_id] = 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# Cart page
def cart(request):

    cart = request.session.get(
        "cart",
        {}
    )

    cart_items = []
    total = Decimal("0.00")

    for product_id, quantity in cart.items():

        product = get_object_or_404(
            MenuItem,
            id=product_id
        )

        subtotal = product.price * quantity

        total += subtotal

        cart_items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal,
        })

    return render(
        request,
        "coffee/cart.html",
        {
            "cart_items": cart_items,
            "total": total,
        }
    )


# Increase cart quantity
def increase_quantity(request, product_id):

    cart = request.session.get(
        "cart",
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        cart[product_id] += 1

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# Decrease cart quantity
def decrease_quantity(request, product_id):

    cart = request.session.get(
        "cart",
        {}
    )

    product_id = str(product_id)

    if product_id in cart:

        if cart[product_id] > 1:
            cart[product_id] -= 1
        else:
            del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")


# Remove product from cart
def remove_from_cart(request, product_id):

    cart = request.session.get(
        "cart",
        {}
    )

    product_id = str(product_id)

    if product_id in cart:
        del cart[product_id]

    request.session["cart"] = cart
    request.session.modified = True

    return redirect("cart")