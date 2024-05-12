# Generated by Django 4.2.7 on 2024-05-12 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0010_category_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Electronics'), ('Clothing', 'Clothing'), ('Home & Kitchen', 'Home & Kitchen'), ('Beauty & Personal Care', 'Beauty & Personal Care'), ('Books', 'Books'), ('Sports & Outdoors', 'Sports & Outdoors'), ('Toys & Games', 'Toys & Games'), ('Health & Wellness', 'Health & Wellness'), ('Automotive', 'Automotive'), ('Others', 'Others')], max_length=100, null=True),
        ),
    ]
