from django.urls import path
from app.views import ProductView,buy_product,payment_success

urlpatterns = [
    path('product/',ProductView.as_view(),name='product-list'),
    path('buy/<int:pk>/', buy_product, name='buy_product'),
    path("payment/success/", payment_success, name="payment_success"),
    #path('webhook/stripe/', stripe_webhook, name='stripe_webhook'),
    
]
