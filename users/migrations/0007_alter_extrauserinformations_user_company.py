# Generated by Django 5.0.1 on 2024-03-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_company_app', '0004_alter_company_contact_person_phone'),
        ('users', '0006_extrauserinformations_user_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrauserinformations',
            name='user_company',
            field=models.ManyToManyField(blank=True, related_name='user_companies', to='user_company_app.company'),
        ),
    ]