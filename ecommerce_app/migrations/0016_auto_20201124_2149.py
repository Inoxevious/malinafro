# Generated by Django 3.0.8 on 2020-11-24 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0015_auto_20201124_2040'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesCategorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(blank=True, max_length=70, null=True)),
                ('long_name', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='sales_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ecommerce_app.SalesCategorie'),
        ),
    ]