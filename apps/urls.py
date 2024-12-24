from django.urls import path, include
from apps.dashboard.views import dashboard, medicine_monthly_counts
from apps.user.views import login, logout_view
from apps.purchase.views import purchase_success_view
urlpatterns = [
    path("dashboard/", dashboard, name="dashboard"),
    path("medicine_monthly_chart/", medicine_monthly_counts, name="medicine_monthly_chart"),
    path("user/", include('apps.user.urls')),
    path("login/", login, name='login'),
    path("logout/", logout_view, name='logout'),
    path("supplier/", include('apps.supplier.urls')),
    path("medicine/", include('apps.medicine.urls')),
    path("purchase/", include('apps.purchase.urls')),
    path("payment/", include('apps.payment.urls')),
    path("invoice/", include('apps.invoice.urls')),
]
