import string
import random
from django.contrib.auth.decorators import login_required  
from sslcommerz_lib import SSLCOMMERZ
from .models import PaymentGateWaySettings
from apps.payment.models import Payment
from django.shortcuts import render, redirect


def sslcommerz_payment_gateway_purchase(request, transaction_data):
    # print('sslcommerz_payment_gateway_purchase sessionkey : ', request.session.session_key)

    # session_key_before = request.session.session_key
    # print('Session Key Before Redirect: ', session_key_before)

    # gateway_auth_details = PaymentGateWaySettings.objects.all().first()
    gateway_auth_details = PaymentGateWaySettings.objects.order_by('id')[1]
    settings = {
        'store_id': gateway_auth_details.store_id,
        'store_pass': gateway_auth_details.store_pass,
        'issandbox': True
    }
    # print('store id : ', settings['store_id'])
    # print('store pass : ', settings['store_pass'])
    sslcommez = SSLCOMMERZ(settings)

    print('transaction data : ', transaction_data)
    post_body = {}
    post_body['total_amount'] = transaction_data['paid_amount']
    post_body['currency'] = "BDT"
    post_body['tran_id'] = transaction_data['transaction_id']
    # post_body['success_url'] = 'http://127.0.0.1:8000/purchase/success/'
    post_body['success_url'] = f"http://127.0.0.1:8000/purchase/success/?value_e={transaction_data['transaction_id']}&value_f={transaction_data['payment_type']}&value_g=purchase"
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



# def sslcommerz_payment_gateway(request, transaction_data):
#     transaction_data = request.session.get('transaction_data')
#     if not transaction_data:
#         return redirect('add_purchase')  # Redirect if no transaction data found

#     gateway_auth_details = PaymentGateWaySettings.objects.first()
#     settings = {
#         'store_id': gateway_auth_details.store_id,
#         'store_pass': gateway_auth_details.store_pass,
#         'issandbox': True,
#     }
#     sslcommerz = SSLCOMMERZ(settings)

#     post_body = {
#         'total_amount': transaction_data['paid_amount'],
#         'currency': "BDT",
#         'tran_id': transaction_data['transaction_id'],
#         'success_url': 'http://127.0.0.1:8000/purchase/success/',
#         'fail_url': 'http://127.0.0.1:8000/dashboard/',
#         'cancel_url': 'http://127.0.0.1:8000/dashboard/',
#         'emi_option': 0,
#         'cus_name': transaction_data['customer_name'],
#         'cus_email': 'shahoraiar2000@gmail.com',
#         'cus_phone': '01711111111',  # Replace with actual phone field from the user profile
#         'cus_add1': 'User address',  # Replace with actual address
#         'cus_city': 'User city',  # Replace with actual city
#         'cus_country': 'Bangladesh',
#         'shipping_method': "NO",
#         'product_name': "Purchase",
#         'product_category': "General",
#         'product_profile': "general",
#     }

#     # response = sslcommerz.createSession(post_body)
#     # print(response)
#     # print('payment url call')
#     # return redirect(response['GatewayPageURL'])

#     response = sslcommerz.createSession(post_body)
#     # print(response)
#     # return JsonResponse(response)
#     return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

# from django.utils.decorators import method_decorator
# Handle SSLCommerz Responses
# @method_decorator(login_required, name='dispatch')
# def sslcommerz_success(request):
#     print('success call 1')
#     tran_id = request.GET.get('tran_id')
#     print('tran id : ', tran_id)
#     if not tran_id:
#         return redirect('add_purchase')  # Redirect if transaction ID is missing

    # Retrieve the transaction data from the database
    # print(f'Successful payment for transaction ID: {tran_id}')
    # Optionally, log and process the transaction here

    # return redirect('dashboard')  # Redirect to a confirmation page
# @method_decorator(login_required, name='dispatch')
# def sslcommerz_success(request):
#     print('success url call 1')
#     transaction_data = request.session.get('transaction_data')
#     print('success transaction data : ', transaction_data)
#     if not transaction_data:
#         print('not have transsation data')
#         return redirect('add_purchase')  # Redirect if no transaction data found

#     # Payment.objects.create(
#     #     customer_name=request.user.username,
#     #     invoice_number=transaction_data['invoice_no'],
#     #     payment_type='sslcommerz',
#     #     transaction_type='purchase',
#     #     amount_paid=transaction_data['paid_amount'],
#     #     status='completed',
#     #     admin_id=request.user,
#     # )
#     print('success url call 2')
#     # del request.session['transaction_data']  # Clear session data
#     return redirect('dashboard') 

# @login_required
# def sslcommerz_fail(request):
#     return render(request, 'payment_failed.html', {'message': 'Payment failed. Please try again.'})

# @login_required
# def sslcommerz_cancel(request):
#     return render(request, 'payment_canceled.html', {'message': 'Payment was canceled by the user.'})



# @login_required 
# def sslcommerz_payment_gateway(request, id, user_id, grand_total):
#     gateway_auth_details = PaymentGateWaySettings.objects.all().first()
#     print('store id : ', gateway_auth_details.store_id)
#     print('sotre pass : ', gateway_auth_details.store_pass)
    
#     settings = {'store_id': gateway_auth_details.store_id,
#                 'store_pass': gateway_auth_details.store_pass, 'issandbox': True}
#     print("heyyyyyyyy ", settings)
#     sslcommez = SSLCOMMERZ(settings)
#     post_body = {}
#     post_body['total_amount'] = grand_total
#     post_body['currency'] = "BDT"
#     post_body['tran_id'] = unique_transaction_id_generator()
#     post_body['success_url'] = 'http://127.0.0.1:8000/dashboard/'
#     post_body['fail_url'] = 'http://127.0.0.1:8000/'
#     post_body['cancel_url'] = 'http://127.0.0.1:8000/dashboard'
#     post_body['emi_option'] = 0
#     post_body['cus_email'] = 'request.user.email'  # Retrieve email from the current user session
#     post_body['cus_phone'] = 'request.user.phone'  # Retrieve phone from the current user session
#     post_body['cus_add1'] = 'request.user.address'  # Retrieve address from the current user session
#     post_body['cus_city'] = 'request.user.city'  # Retrieve city from the current user session
#     post_body['cus_country'] = 'Bangladesh'
#     post_body['shipping_method'] = "NO"
#     post_body['multi_card_name'] = ""
#     post_body['num_of_item'] = 1
#     post_body['product_name'] = "Test"
#     post_body['product_category'] = "Test Category"
#     post_body['product_profile'] = "general"

#     # OPTIONAL PARAMETERS
#     # post_body['value_a'] = id
#     # post_body['value_b'] = user_id
#     # post_body['value_c'] = 'email'

#     response = sslcommez.createSession(post_body)
#     print(response)
#     # return JsonResponse(response)
#     return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

