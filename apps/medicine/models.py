from django.db import models
from system.generic.models import BaseModel
from apps.user.models import User
from apps.supplier.models import Supplier
# Create your models here.

class Medicine(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    generic_name = models.CharField(max_length=255, null=True, blank=True)
    strength = models.CharField(max_length=255, null=True, blank=True)
    shelf = models.CharField(max_length=255, blank=True, null=True)
    details = models.CharField(max_length=255, blank=True, null=True)
    batch = models.CharField(max_length=255, blank=True, null=True)
    expire_date = models.DateField(null=True, blank=True) 
    stock = models.PositiveIntegerField(default=0, blank=True, null=True) 
    price =  models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    supplier_name = models.ForeignKey(Supplier, on_delete=models.CASCADE, blank=True, null=True)
    supplier_price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=8, default='1')
    box_size = models.ForeignKey('Leaf', on_delete=models.CASCADE, blank=True, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    type = models.ForeignKey('Type', on_delete=models.CASCADE, blank=True, null=True)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'medicine'

class Category(BaseModel): # Anti Allergic
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=8, default='1')
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'medicine_category'

class Unit(BaseModel): # Box, Pack, Dose
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=8, default='1')
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'medicine_unit'

class Type(BaseModel): # Capsule
    name = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=8, default='1')
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'medicine_type'

class Leaf(BaseModel): # BOX 24
    name = models.CharField(max_length=255, unique=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=8, default='1')
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    created_by = models.IntegerField(default=0, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    updated_by = models.IntegerField(default=0, blank=True, null=True)
    class Meta:
        db_table = 'medicine_leaf'
