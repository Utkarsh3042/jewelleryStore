# Generated by Django 5.1 on 2024-12-23 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_slug',
        ),
    ]
