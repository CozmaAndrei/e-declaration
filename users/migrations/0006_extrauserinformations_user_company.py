# Generated by Django 5.0.1 on 2024-03-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_company_app', '0004_alter_company_contact_person_phone'),
        ('users', '0005_remove_extrauserinformations_user_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='extrauserinformations',
            name='user_company',
            field=models.ManyToManyField(blank=True, related_name='userCompany', to='user_company_app.company'),
        ),
    ]