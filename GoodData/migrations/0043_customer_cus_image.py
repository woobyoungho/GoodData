# Generated by Django 3.1.1 on 2020-10-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0042_auto_20201029_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cus_image',
            field=models.ImageField(blank=True, upload_to='static/customer_img'),
        ),
    ]