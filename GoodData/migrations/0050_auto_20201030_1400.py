# Generated by Django 3.1.1 on 2020-10-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0049_auto_20201030_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_image',
            field=models.ImageField(null=True, upload_to='static/customer_img'),
        ),
    ]