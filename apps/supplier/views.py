from django.shortcuts import render, redirect
from apps.supplier.forms import SupplierForm
from apps.supplier.models import Supplier
from system.utils import paginate_data
from django.http import JsonResponse
from django.utils.safestring import mark_safe
# Create your views here.
def supplier(request):
    if request.method == 'POST':
        data = Supplier.objects.all()
        print('Supplier data : ', data)
        response_data, page_data = paginate_data(Supplier, data, request)
        count = 0
        for data in page_data:
            count += 1
            status_html = 'InActivate'
            if data.status=='1':
                status_html = 'Activate'
            response_data['data'].append({
                'count' : count,
                'id' : data.id,
                'name' : data.name,
                'phone' : data.phone_no,
                'email' : data.email,
                'address' : data.address,
                'city' : data.city,
                'state' : data.state,
                'balance' : data.balance,
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/supplier/supplier_list.html')

def add(request):
    context = {}
    if request.method == 'POST':
        form = SupplierForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            return redirect('supplier_list')  
        else:
            print('Form Errors: ', form.errors)  
    else:
        form = SupplierForm(request=request)  
    
    context['form'] = form
    return render(request, 'backend/main/supplier/add.html', context=context)

def edit(reqeust, id=None):
    pass
