# Generated by Django 3.1.1 on 2020-11-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0051_notice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='cus_image',
            field=models.ImageField(blank=True, null=True, upload_to='static/customer_img'),
        ),
    ]
