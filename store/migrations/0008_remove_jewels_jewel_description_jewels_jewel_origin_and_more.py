# Generated by Django 5.1 on 2025-01-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_jewels_jewel_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jewels',
            name='jewel_description',
        ),
        migrations.AddField(
            model_name='jewels',
            name='jewel_origin',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewels',
            name='jewel_size',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='jewels',
            name='jewel_weight',
            field=models.TextField(null=True),
        ),
    ]
