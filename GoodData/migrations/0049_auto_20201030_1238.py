# Generated by Django 3.1.1 on 2020-10-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0048_auto_20201030_1223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_image',
            field=models.ImageField(blank=True, default='media/customer_img/profile_photo.jpg', null=True, upload_to='media/customer_img'),
        ),
    ]