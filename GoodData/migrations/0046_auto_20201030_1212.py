# Generated by Django 3.1.1 on 2020-10-30 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0045_auto_20201030_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_image',
            field=models.ImageField(blank=True, default='static/customer_img/profile_photo.jpg', upload_to='media/customer_img'),
        ),
    ]
