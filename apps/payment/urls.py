from django.urls import path
from apps.purchase.views import *
from apps.payment.views import *
# from apps.payment.sslcommerz import sslcommerz_payment_gateway, sslcommerz_success
urlpatterns = [
    # path('', sslcommerz_payment_gateway, name='sslcommerz_payment_gateway'),
    # path('success/', sslcommerz_success, name='sslcommerz_success'),
    path('', payment_list, name='payment_list')
]
