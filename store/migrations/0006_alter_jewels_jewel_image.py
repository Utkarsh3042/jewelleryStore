# Generated by Django 5.1 on 2024-12-24 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_alter_jewels_jewel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jewels',
            name='jewel_image',
            field=models.ImageField(upload_to='store/jewellery_images/'),
        ),
    ]
