# Generated by Django 5.0.1 on 2024-02-16 13:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication_app', '0021_delete_companyuser'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='users',
            field=models.ManyToManyField(related_name='company', to=settings.AUTH_USER_MODEL),
        ),
    ]
