# Generated by Django 3.0.8 on 2020-11-23 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0010_auto_20201123_1345'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product_Material_Colors',
            new_name='ProductMaterialMainColor',
        ),
    ]
