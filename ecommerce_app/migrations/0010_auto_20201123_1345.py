# Generated by Django 3.0.8 on 2020-11-23 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0009_collection_banner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Material_Colors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=191)),
                ('isAvailable', models.BooleanField(blank=True, default=False, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='major_color',
        ),
        migrations.AddField(
            model_name='product',
            name='major_colors',
            field=models.ManyToManyField(blank=True, null=True, to='ecommerce_app.Product_Material_Colors'),
        ),
    ]
