# Generated by Django 5.0.1 on 2024-02-15 16:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0020_companyuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompanyUser',
        ),
    ]
