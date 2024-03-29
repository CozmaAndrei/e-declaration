# Generated by Django 5.0.1 on 2024-03-02 08:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraUserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_birth', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='extra_info', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Extra User Informations',
                'verbose_name_plural': 'Extra User Informations',
                'db_table': 'Extra User Informations',
            },
        ),
    ]
