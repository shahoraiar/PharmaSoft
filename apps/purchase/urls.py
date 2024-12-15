from django.urls import path
from apps.purchase.views import *
# from apps.payment.sslcommerz import sslcommerz_payment_gateway, sslcommerz_success
urlpatterns = [
    path('', purchase_list, name="purchase_list"),
    path("add/", purchase, name="add_purchase"),
    path('fetch_medicines_by_supplier/', fetch_medicines_by_supplier, name='fetch_medicines_by_supplier'),
    path('save_purchase_data/', save_purchase_data, name='save_purchase_data'),
    path('process/', purchase_process, name='purchase_process'),
    path('success/', purchase_success_view, name='purchase_success_view'),
    # path('sslcommerz/', sslcommerz_payment_gateway, name='sslcommerz_payment_gateway'),
    # path('sslcommerz/success/', sslcommerz_success, name='sslcommerz_success'),
]
