# Generated by Django 5.0.1 on 2024-04-02 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0007_alter_extendcompanymodel_declaration_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendcompanymodel',
            name='declaration_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
