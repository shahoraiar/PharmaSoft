from django.shortcuts import render, redirect, get_object_or_404
from apps.permission.models import Role
from system.utils import paginate_data
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.contrib import messages
from apps.user.models import User
from apps.user.forms import UserAddForm
from apps.permission.forms import RoleAddForm
from django.contrib.auth import login as system_login 
from system.auth import authenticate_user
from system.middleware.thread_local import _thread_local
from django.contrib.auth import logout
# Create your views here.
def user_list(request):
    if request.method == 'POST':
        data = User.objects.all()
        # print('user data : ', data)
        print('thread local user : ', _thread_local)
        print('thread local user : ', _thread_local.user)
        print('thread local user : ', _thread_local.user.id) 
        response_data, page_data = paginate_data(User, data, request)
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
                'email' : data.email,
                'phone' : data.phone_no,
                'user_role' : data.user_role_name,
                'status' : mark_safe(status_html),
                'action' : ''
            })
        return JsonResponse(response_data)
    return render(request, 'backend/system/user/user_list.html')

def user_add(request):
    context = {}
    roles = Role.objects.all()  
    # for role in roles:
    #     print('roles : ', role.name)
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            print('data : ', form.cleaned_data)
            form.save()
            messages.success(request, 'Successfully saved!')
            return redirect('user_list')  
        else:
            messages.error(request, 'Cannot save. Please fill up the required inputs.')
            print('Form Errors: ', form.errors)  
    else:
        form = UserAddForm()  
    
    context['form'] = form
    context['roles'] = roles
    return render(request, 'backend/system/user/user_add.html', context=context)

# def login(request):
#     context = {}

#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         print(f'email: {email} password: {password}')

#         user = authenticate_user(request, email=email, password=password)
#         print(user)
        
#         if user is not None:
#             request.session['logged_in_pass'] = True
#             system_login(request, user)  # Assuming you have a system_login function for post-login actions
#             return redirect('dashboard')  # Redirect to the dashboard after successful login
#         else:
#             context['error'] = 'Invalid email or password'
#             # Add error to the context for each field
#             context['email_error'] = 'Invalid email or email not found' if 'email not found' in context.get('error', '') else ''
#             context['password_error'] = 'Invalid password' if 'password wrong' in context.get('error', '') else ''
#             print('error:', context['error'])

#     return render(request, 'frontend/user_auth/signin1.html', context)

def login(request):
    print('login sessionkey : ', request.session.session_key)
    context={}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(f'email : {email} password : {password}')
        user = authenticate_user(request, email=email, password=password)
        print(user)
        # print(user.is_active) 
        if user is not None:
            request.session['logged_in_pass'] = True
            system_login(request, user)
            messages.success(request, 'Wellcome To Medicine List')
            return redirect('medicine_list')  
        else:
            messages.error(request, 'Email or Password wrong')
            context['error'] = 'Invalid email or password'
            print('error : ', context['error'])
    return render(request, 'frontend/user_auth/signin.html', context=context)

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('login')

def role(request):
    return render(request, 'backend/system/role/role.html')

def role_json(request, *args, **kwargs):
    if request.method == 'POST':
        data = Role.objects.all()
        print('role data : ', data)
        response_data, page_data = paginate_data(Role, data, request)
        
        count = 0
        for data in page_data :
            count += 1
            # Edit link with a space after
            action_html = f'<a href="/user/role/edit/{data.id}" style="margin-right: 5px; font-size: 22px;"><i class="fas fa-edit"></i></a>'
            
            # Delete link with a space before and after
            action_html += f'<a href="/user/role/delete/{data.id}" style="margin-left: 5px; font-size: 22px;"><i class="fa-solid fa-trash"></i></a>'
            
            response_data['data'].append({
                'id' : data.id,
                'name' : data.name,
                'slug' : data.slug,
                'status' : data.status,
                'created_at' : data.created_at,
                'updated_at' : data.updated_at,
                'created_by' : data.created_by,
                'updated_by' : data.updated_by,
                'action' : mark_safe(action_html),
            })
        return JsonResponse(response_data)
    
def role_add(request):
    context = {}
    if request.method == 'POST':
        form = RoleAddForm(request.POST)
        if form.is_valid():
            # print('data : ', form.cleaned_data)
            form.save()  
            return redirect('role_list')  
        else:
            print('Form Errors: ', form.errors)  
    else:
        form = RoleAddForm()  
    
    context['form'] = form
    return render(request, 'backend/system/role/add.html', context=context)

def role_edit(request, id=None):
    context = {}
    
    user_role = get_object_or_404(Role, id=id) if id else None
    
    if request.method == 'POST':
        form = RoleAddForm(request.POST, instance=user_role)
        if form.is_valid():
            print('edit : ', form.cleaned_data)
            form.save()  
            return redirect('role_list') 
    else:
        form = RoleAddForm(instance=user_role)  
        
    context['form'] = form
    context['role_data'] = Role.objects.all()  
    
    return render(request, 'backend/system/role/edit.html', context)

def role_delete(request, id=None):
    if id:
        role = get_object_or_404(Role, id=id)
        
        role.delete()
        
        messages.success(request, f'Role "{role.name}" has been successfully deleted.')

    return redirect('role_list')
   
