# Generated by Django 5.1 on 2025-01-02 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_delete_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewels',
            name='jewel_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
