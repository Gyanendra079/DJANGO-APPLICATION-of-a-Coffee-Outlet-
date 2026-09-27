from django.db import models


class MenuItem(models.Model):

    CATEGORY_CHOICES = [
        ("Coffee", "Coffee"),
        ("Tea", "Tea"),
        ("Cold Drinks", "Cold Drinks"),
        ("Snacks", "Snacks"),
        ("Desserts", "Desserts"),
    ]

    name = models.CharField(max_length=100)

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    image = models.URLField(
        blank=True
    )

    is_available = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.name


class Order(models.Model):

    STATUS_CHOICES = [
        ("Received", "Received"),
        ("Preparing", "Preparing"),
        ("Ready", "Ready"),
        ("Out for Delivery", "Out for Delivery"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    ]

    customer_name = models.CharField(
        max_length=100
    )

    phone = models.CharField(
        max_length=20
    )

    email = models.EmailField(
        blank=True
    )

    address = models.TextField()

    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="Received"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Order #{self.id} - {self.customer_name}"


class OrderItem(models.Model):

    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name="items"
    )

    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.PROTECT
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f"{self.menu_item.name} × {self.quantity}"