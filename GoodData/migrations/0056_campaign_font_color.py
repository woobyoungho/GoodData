# Generated by Django 3.1.1 on 2020-11-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0055_remove_customer_cus_rrn'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='font_color',
            field=models.CharField(choices=[('red', 'red'), ('green', 'green'), ('blue', 'blue')], default=1, max_length=30),
            preserve_default=False,
        ),
    ]
