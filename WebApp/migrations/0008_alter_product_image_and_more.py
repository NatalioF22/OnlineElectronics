# Generated by Django 4.2.2 on 2023-07-03 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0007_alter_product_product_description_productpost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(blank=True, default='', max_length=5000, null=True),
        ),
    ]