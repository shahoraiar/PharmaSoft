# Generated by Django 5.1.3 on 2024-11-16 18:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("medicine", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="leaf",
            name="amount",
        ),
        migrations.AddField(
            model_name="leaf",
            name="quantity",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
