# Generated by Django 5.0.1 on 2024-05-06 21:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0011_alter_company_company_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_manager',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='company_manager', to=settings.AUTH_USER_MODEL),
        ),
    ]
