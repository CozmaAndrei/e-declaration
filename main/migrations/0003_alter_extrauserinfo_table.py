# Generated by Django 5.0.1 on 2024-03-02 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_extrauserinfo_user'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='extrauserinfo',
            table='extrauser',
        ),
    ]
