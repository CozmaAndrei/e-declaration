# Generated by Django 5.0.1 on 2024-03-21 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_declaration', '0005_remove_extendcompanymodel_default_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendcompanymodel',
            name='declaration_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
