# Generated by Django 5.1 on 2025-01-03 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_remove_jewels_jewel_image_jewels_jewel_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewels',
            name='jewel_name',
            field=models.CharField(max_length=50),
        ),
    ]
