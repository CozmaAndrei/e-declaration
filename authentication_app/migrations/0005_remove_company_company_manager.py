# Generated by Django 5.0.1 on 2024-02-12 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0004_alter_company_company_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='company_manager',
        ),
    ]
