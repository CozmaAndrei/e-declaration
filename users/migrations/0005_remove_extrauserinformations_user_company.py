# Generated by Django 5.0.1 on 2024-03-05 14:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_extrauserinformations_user_company'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extrauserinformations',
            name='user_company',
        ),
    ]
