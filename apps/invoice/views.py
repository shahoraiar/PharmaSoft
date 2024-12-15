from django.shortcuts import render, redirect
from apps.supplier.models import Supplier
from apps.purchase.models import Purchase
from system.utils import paginate_data
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.views.decorators.csrf import csrf_exempt
from apps.medicine.models import Medicine, Leaf
import json
from apps.payment.sslcommerz import sslcommerz_payment_gateway_purchase
from apps.payment.models import Payment
from apps.supplier.models import Supplier
from apps.invoice.models import Invoice
from datetime import datetime

def generate_invoice_no():
    # Get the current year (last two digits) and month
    current_year = datetime.now().strftime('%y')  # e.g., '24' for 2024
    current_month = datetime.now().strftime('%m')  # e.g., '11' for November

    # Retrieve the last Payment object's ID, default to 0 if no payments exist
    try:
        last_payment = Payment.objects.latest('id')
        last_id = last_payment.id
    except Payment.DoesNotExist:
        last_id = 0

    # Increment the last ID and pad it with leading zeros
    new_id = last_id + 1
    padded_id = str(new_id).zfill(8)  # Ensures the ID is always 8 digits

    # Return the generated invoice number
    return f"{current_year}{current_month}{padded_id}"

# Create your views here.
def invoice_list(request):
    if request.method == 'POST':
        data = Invoice.objects.all()
        print('Invoice data : ', data)
        response_data, page_data = paginate_data(Invoice, data, request)
        count = 0
        for data in page_data:
            count += 1
            response_data['data'].append({
                'count' : count,
                'id' : data.id,
                'customer_name' : data.customer_name,
                'invoice_no' : data.invoice_no,
                'medicine_info' : data.medicine_info.name,
                'quantity' : data.box_quantity,
                'sell_price' : data.sell_price,
                'total_price' : data.total_price,
                'paid_amount' : data.paid_amount,
                'due_amount' : data.due_amount,
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/invoice/invoice_list.html')

def invoice_add(request):
    context={}
    # print('purchase sessionkey : ', request.session.session_key)
    medicines = Medicine.objects.all()
    leaf = Leaf.objects.all()
    invoice_no = generate_invoice_no()
    payment_types = {'1':'handcash', '2':'sslcommerz'}
    context = {
        'medicines' : medicines,
        'payment_type': payment_types,
        'invoice_no': invoice_no,
        'leaf': leaf,
        'transaction_type': 'invoice'
    }
    # print('purchase sessionkey : ', request.session.session_key)
    return render(request, 'backend/main/invoice/add_invoice.html', context=context)

def save_invoice_data(request):
    if request.method == "POST":
        # Retrieve form data from the request
        customer_name = request.POST.get("name")
        invoice_no = request.POST.get("invoice_no")
        details = request.POST.get("details")
        payment_type = request.POST.get("payment_type")
        
        # Retrieve the totals data from the request
        sub_total = request.POST.get("sub_total")
        discount = request.POST.get("discount")
        grand_total = request.POST.get("grand_total")
        paid_amount = request.POST.get("paid_amount")
        due_amount = request.POST.get("due_amount")
        quantity = request.POST.get("quantity")

        # Debug: Print the received totals
        print("Sub Total:", sub_total)
        print("Discount:", discount)
        print("Grand Total:", grand_total)
        print("Paid Amount:", paid_amount)
        print("Due Amount:", due_amount)

        # Retrieve and prepare the medicines data
        medicine_names = request.POST.getlist("medicine_name[]")
        quantities = request.POST.getlist("quantity[]")
        prices = request.POST.getlist("price[]")
        total_prices = request.POST.getlist("total_price[]")

        # Debug: Print the received data
        # print("medicine_names:", supplier_id)
        # print("Invoice No:", invoice_no)
        # print("Details:", details)
        # print("Payment Type:", payment_type)
        # print("Medicine Quantity: ", box_quantity)


        # Store the purchase data
        for i in range(len(medicine_names)):
            try:
                # Get related Medicine and Leaf objects
                medicine = Medicine.objects.get(id=medicine_names[i])
                
                # Create a new Purchase record
                invoice = Invoice(
                    customer_name=customer_name,
                    invoice_no=invoice_no,
                    details=details,
                    payment_type=payment_type,
                    medicine_info=medicine,
                    box_quantity=quantities[i],
                    sell_price=prices[i],
                    total_price=total_prices[i],
                    paid_amount=paid_amount,
                    due_amount=due_amount
                )

                # Save the purchase to the database
                invoice.save()

                medicine.stock -= int(quantities[i])
                medicine.save()

            except Medicine.DoesNotExist:
                return JsonResponse({"status": "error", "message": f"Medicine with ID {medicine_names[i]} not found."})

        # Return a response after saving the data
        return redirect('add_invoice')

    # If not a POST request, return an error
    return JsonResponse({"status": "error", "message": "Invalid request method."})
