# Generated by Django 3.1.1 on 2020-10-07 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0014_campaign_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='image',
            field=models.ImageField(upload_to='campaign_img'),
        ),
    ]
