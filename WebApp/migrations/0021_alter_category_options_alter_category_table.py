# Generated by Django 4.2.7 on 2024-05-12 17:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0020_alter_category_options_remove_category_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelTable(
            name='category',
            table='categories',
        ),
    ]
