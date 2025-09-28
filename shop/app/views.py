import uuid
import stripe
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib import messages
from django.urls import reverse

from .models import Product, OrderProduct

stripe.api_key = settings.STRIPE_SECRET_KEY

# -----------------------------
# Product list + orders display
# -----------------------------
class ProductView(ListView):
    model = Product
    template_name = "app/product_list.html"
    context_object_name = "products"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['orders'] = OrderProduct.objects.all().order_by('-id')  # latest orders first
        return context

# -----------------------------
# Buy product view
# -----------------------------
def buy_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        try:
            quantity = int(request.POST.get("quantity", 1))
        except ValueError:
            quantity = 1

        if quantity < 1:
            messages.error(request, "Quantity must be at least 1.")
            return redirect("product-list")

        # Stripe idempotency key prevents accidental double charges
        idempotency_key = str(uuid.uuid4())

        # Create Stripe Checkout session
        session = stripe.checkout.Session.create(
            payment_method_types=["card"],
            line_items=[{
                "price_data": {
                    "currency": "inr",
                    "product_data": {"name": product.title},
                    "unit_amount": int(product.selling_price * 100),
                },
                "quantity": quantity,
            }],
            mode="payment",
            success_url=request.build_absolute_uri(reverse("payment_success")) + "?session_id={CHECKOUT_SESSION_ID}",
            cancel_url=request.build_absolute_uri(reverse("product-list")),
            idempotency_key=idempotency_key
        )

        return redirect(session.url, code=303)

    return redirect("product-list")

# -----------------------------
# Payment success
# -----------------------------
def payment_success(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        messages.error(request, "Payment failed or canceled.")
        return redirect("product-list")

    session = stripe.checkout.Session.retrieve(session_id)
    line_items = stripe.checkout.Session.list_line_items(session_id, limit=100)

    for item in line_items.data:
        product_name = item.description or item.price.product.name
        quantity = item.quantity
        amount_total = item.amount_total / 100 if hasattr(item, 'amount_total') else session.amount_total / 100

        product = Product.objects.filter(title=product_name).first()
        if product:
            # Create new order for every purchase
            OrderProduct.objects.create(
                product=product,
                quantity=quantity,
                total_price=amount_total
            )

    messages.success(request, "✅ Payment successful! Your orders have been recorded.")
    return redirect("product-list")
