from django.shortcuts import render, redirect
from apps.medicine.forms import MedicinAddForm, CategoryForm, UnitForm, TypeForm, LeafForm
from apps.medicine.models import Medicine, Category, Unit, Type, Leaf
from system.utils import paginate_data
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.contrib import messages
from apps.supplier.models import Supplier

# Create your views here.

def medicine(request):
    if request.method == 'POST':
        data = Medicine.objects.all()
        print('Medicine data : ', data)
        response_data, page_data = paginate_data(Category, data, request)
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
                'generic_name' : data.generic_name,
                'strength' : data.strength,
                'shelf' : data.shelf,
                'supplier_name' : data.supplier_name.name,
                'category' : data.category.name,
                'stock' : data.stock,
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/medicine/medicine_list.html')

def medicine_add(request):
    context = {}
    supplier = Supplier.objects.all()
    category = Category.objects.all()
    unit = Unit.objects.all()
    type = Type.objects.all()
    leaf = Leaf.objects.all()
    if request.method == 'POST':
        form = MedicinAddForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Successfully saved!")
            return redirect('medicine_list')  
        else:
            print('Form Errors: ', form.errors)  
            context['errors'] = form.errors
            messages.error(request, 'Cannot save. Please fill up the required inputs.')
    else:
        form = MedicinAddForm(request=request) 
        
    context['form'] = form
    context['suppliers'] = supplier
    context['categorys'] = category
    context['units'] = unit
    context['types'] = type
    context['leafs'] = leaf
    
    return render(request, 'backend/main/medicine/medicine_add.html', context=context)
         

def category(request):
    if request.method == 'POST':
        data = Category.objects.all()
        print('Category data : ', data)
        response_data, page_data = paginate_data(Category, data, request)
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
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/medicine/category/category_list.html')

def category_add(request):
    context = {}
    if request.method == 'POST':
        form = CategoryForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Successfully saved!")
            return redirect('category_list')  
        else:
            # print('Form Errors: ', form.errors)  
            context['errors'] = form.errors
            messages.error(request, 'Cannot save. Please fill up the required inputs.')
    else:
        form = CategoryForm(request=request) 
         
        
    
    context['form'] = form
    return render(request, 'backend/main/medicine/category/category_add.html', context=context)

def unit_list(request):
    if request.method == 'POST':
        data = Unit.objects.all()
        print('Unit data : ', data)
        response_data, page_data = paginate_data(Unit, data, request)
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
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/medicine/unit/unit_list.html')

def unit_add(request):
    context = {}
    if request.method == 'POST':
        form = UnitForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Successfully saved!")
            return redirect('unit_list')  
        else:
            # print('Form Errors: ', form.errors) 
            context['errors'] = form.errors 
            messages.error(request, 'Cannot save. Please fill up the required inputs.')
    else:
        form = UnitForm(request=request)  
    
    context['form'] = form
    return render(request, 'backend/main/medicine/unit/unit_add.html', context=context)

def type_list(request):
    if request.method == 'POST':
        data = Type.objects.all()
        print('Type data : ', data)
        response_data, page_data = paginate_data(Type, data, request)
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
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/medicine/type/type_list.html')

def type_add(request):
    context = {}
    if request.method == 'POST':
        form = TypeForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Successfully saved!")
            return redirect('type_list')  
        else:
            # print('Form Errors: ', form.errors)  
            context['errors'] = form.errors
            messages.error(request, 'Cannot save. Please fill up the required inputs.')
    else:
        form = TypeForm(request=request)  
    
    context['form'] = form
    return render(request, 'backend/main/medicine/type/type_add.html', context=context)

def leaf_list(request):
    if request.method == 'POST':
        data = Leaf.objects.all()
        print('Leaf data : ', data)
        response_data, page_data = paginate_data(Type, data, request)
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
                'quantity' : data.quantity,
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/main/medicine/leaf/leaf_list.html')

def leaf_add(request):
    context = {}
    if request.method == 'POST':
        form = LeafForm(request.POST, request=request)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save(commit=True)
            messages.success(request, "Successfully saved!")
            return redirect('leaf_list')  
        else:
            print('Form Errors: ', form.errors)  
            messages.error(request, "Failed to save. Please check the errors.")
            context['errors'] = form.errors
    else:
        form = LeafForm(request=request)  
    
    context['form'] = form
    return render(request, 'backend/main/medicine/leaf/leaf_add.html', context=context)
