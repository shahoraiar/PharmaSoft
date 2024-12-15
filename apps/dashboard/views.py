from django.shortcuts import render

# Create your views here.
def dashboard(request):
    print('dashboard sessionkey : ', request.session.session_key)
    return render(request, 'backend/dashboard/dashboard.html')
