from django import forms


class CheckoutForm(forms.Form):

    customer_name = forms.CharField(
        max_length=100,
        label="Name"
    )

    phone = forms.CharField(
        max_length=20,
        label="Phone"
    )

    email = forms.EmailField(
        required=False,
        label="Email"
    )

    address = forms.CharField(
        widget=forms.Textarea,
        label="Address"
    )

class OrderTrackingForm(forms.Form):
    order_id = forms.IntegerField(
        label="Order ID",
        min_value=1
    )

    phone = forms.CharField(
        max_length=20,
        label="Phone Number"
    )