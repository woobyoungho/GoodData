# Generated by Django 3.1.1 on 2020-11-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0058_auto_20201116_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='font_color',
            field=models.CharField(choices=[('navy', 'navy'), ('aqua', 'aqua'), ('silver', 'silver'), ('teal', 'teal'), ('red', 'red'), ('purple', 'purple'), ('yellow', 'yellow'), ('gray', 'gray'), ('fuchsia', 'fuchsia'), ('black', 'black'), ('green', 'green'), ('maroon', 'maroon'), ('lime', 'lime'), ('blue', 'blue'), ('-', ''), ('olive', 'olive')], default='', max_length=30),
        ),
    ]
