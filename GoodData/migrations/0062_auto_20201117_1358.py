# Generated by Django 3.1.1 on 2020-11-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0061_auto_20201117_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='font_color',
            field=models.CharField(choices=[('olive', 'olive'), ('fuchsia', 'fuchsia'), ('green', 'green'), ('black', 'black'), ('red', 'red'), ('#edffff', 'lime'), ('purple', 'purple'), ('aqua', 'aqua'), ('maroon', 'maroon'), ('yellow', 'yellow'), ('blue', 'blue'), ('navy', 'navy'), ('silver', 'silver'), ('teal', 'teal'), ('gray', 'gray')], default='', max_length=30),
        ),
    ]