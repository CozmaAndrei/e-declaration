# Generated by Django 5.0.1 on 2024-03-05 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_company_app', '0002_alter_company_contact_person_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='contact_person_phone',
            field=models.CharField(blank=True, default=' - ', max_length=25),
        ),
    ]