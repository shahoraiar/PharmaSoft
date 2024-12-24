import string
import random
from django.contrib.auth.decorators import login_required  
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateWaySettings
from apps.payment.models import Payment
from django.shortcuts import render, redirect


def sslcommerz_payment_gateway_purchase(request, transaction_data):
    gateway_auth_details = PaymentGateWaySettings.objects.order_by('id')[1]
    settings = {
        'store_id': gateway_auth_details.store_id,
        'store_pass': gateway_auth_details.store_pass,
        'issandbox': True
    }
    sslcommez = SSLCOMMERZ(settings)

    print('transaction data : ', transaction_data)
    post_body = {}
    post_body['total_amount'] = transaction_data['paid_amount']
    post_body['currency'] = "BDT"
    post_body['tran_id'] = transaction_data['transaction_id']
    # post_body['success_url'] = 'http://127.0.0.1:8000/purchase/success/'
    post_body['success_url'] = f"http://127.0.0.1:8000/purchase/success/?value_e={transaction_data['transaction_id']}&value_f={transaction_data['payment_type']}&value_g={transaction_data['billing_type']}"
    post_body['fail_url'] = 'http://127.0.0.1:8000/user/'
    post_body['cancel_url'] = 'http://127.0.0.1:8000/dahboard/'
    post_body['emi_option'] = 0
    post_body['cus_email'] = 'shahora@gmail.com'  # Retrieve email from the current user session
    post_body['cus_phone'] = '01739935012'  # Retrieve phone from the current user session
    post_body['cus_add1'] = 'savar'  # Retrieve address from the current user session
    post_body['cus_city'] = 'dhaka'  # Retrieve city from the current user session
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"
    post_body['secret_key'] = '558899'

    # OPTIONAL PARAMETERS
    post_body['value_a'] = transaction_data['customer_name']
    post_body['value_b'] = transaction_data['invoice_no']
    post_body['value_c'] = transaction_data['details']
    post_body['value_d'] = transaction_data['paid_amount']
    # post_body['value_e'] = transaction_data['transaction_id']
    # post_body['value_f'] = transaction_data['payment_type']
    # post_body['value_g'] = 'purchase'

 
    response = sslcommez.createSession(post_body)
    # print('response : ', response)
    # return response["GatewayPageURL"]
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]



