# Generated by Django 5.0.1 on 2024-02-25 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0025_remove_company_company_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='users',
            new_name='managers',
        ),
    ]
