# Generated by Django 5.1.3 on 2024-11-16 05:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(blank=True, default=0, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "admin_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "medicine_category",
            },
        ),
        migrations.CreateModel(
            name="Leaf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("amount", models.IntegerField(blank=True, max_length=255, null=True)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(blank=True, default=0, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "admin_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "medicine_leaf",
            },
        ),
        migrations.CreateModel(
            name="Type",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(blank=True, default=0, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "admin_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "medicine_type",
            },
        ),
        migrations.CreateModel(
            name="Unit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(blank=True, default=0, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "admin_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "db_table": "medicine_unit",
            },
        ),
        migrations.CreateModel(
            name="Medicine",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "generic_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("strength", models.CharField(blank=True, max_length=255, null=True)),
                ("shelf", models.CharField(blank=True, max_length=255, null=True)),
                ("details", models.CharField(blank=True, max_length=255, null=True)),
                ("batch", models.CharField(blank=True, max_length=255, null=True)),
                ("expire_date", models.DateField(blank=True, null=True)),
                (
                    "stock",
                    models.PositiveIntegerField(blank=True, default=0, null=True),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                (
                    "supplier_price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=15, null=True
                    ),
                ),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(blank=True, default=0, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "admin_id",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "box_size",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medicine.leaf",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medicine.category",
                    ),
                ),
                (
                    "type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medicine.type",
                    ),
                ),
                (
                    "unit",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="medicine.unit",
                    ),
                ),
            ],
            options={
                "db_table": "medicine",
            },
        ),
    ]