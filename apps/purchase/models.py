from django.db import models
from system.generic.models import BaseModel
from apps.medicine.models import Medicine, Leaf
from apps.supplier.models import Supplier
from apps.user.models import User
# Create your models here.

class Purchase(BaseModel):
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    invoice_no = models.CharField(max_length=255, blank=True, null=True)
    details = models.TextField(blank=True, null=True)  # Removed max_length, since TextField doesn't require it
    payment_type = models.CharField(max_length=50, blank=True, null=True)  # You may consider using choices
    medicine_info = models.ForeignKey(Medicine, on_delete=models.CASCADE, blank=True, null=True)
    batch_id = models.CharField(max_length=255, blank=True, null=True)
    expire_date = models.DateField(blank=True, null=True)
    leaf = models.ForeignKey(Leaf, on_delete=models.CASCADE, blank=True, null=True)
    
    # Changed to PositiveIntegerField for quantities
    box_quantity = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_quantity = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    # Changed to DecimalField for prices
    supplier_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    box_mrp = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    total_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    paid_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    due_amount = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    status = models.CharField(max_length=8, default='1')
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    
    class Meta:
        db_table = 'purchase'