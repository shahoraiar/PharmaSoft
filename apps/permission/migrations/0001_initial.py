# Generated by Django 5.1.3 on 2024-11-11 12:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Permission",
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
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "user_permission",
            },
        ),
        migrations.CreateModel(
            name="Role",
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
                ("name", models.CharField(default="General", max_length=255)),
                ("slug", models.SlugField(blank=True, max_length=255)),
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(default=0)),
            ],
            options={
                "db_table": "user_role",
            },
        ),
        migrations.CreateModel(
            name="RolePermission",
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
                ("status", models.CharField(default="1", max_length=8)),
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("created_by", models.IntegerField(default=0)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                ("updated_by", models.IntegerField(default=0)),
                (
                    "permission_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permission.permission",
                    ),
                ),
                (
                    "role_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="permission.role",
                    ),
                ),
            ],
            options={
                "db_table": "role_permission",
            },
        ),
    ]