# Generated by Django 3.0.8 on 2020-11-24 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce_app', '0016_auto_20201124_2149'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='collecion_category',
            field=models.CharField(blank=True, choices=[('just_in', 'just_in'), ('summer_look', 'summer_look'), ('lovers_show_off', 'lovers_show_off'), ('ambitious_personalities', 'ambitious_personalities'), ('ambitious_kidz', 'ambitious_kidz'), ('fashion_blog', 'fashion_blog')], default='just_in', max_length=50, null=True),
        ),
    ]
