# Generated by Django 3.1.1 on 2020-11-20 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0064_auto_20201120_1651'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='font_color',
        ),
        migrations.AddField(
            model_name='campaign',
            name='background_color',
            field=models.CharField(choices=[('#c7cfff', 'aqua'), ('#b3bef9', 'olive'), ('##e2e6fb', 'lime'), ('#bde6f3', 'teal'), ('#fdeaea', 'purple'), ('#d0d0d0', 'navy'), ('#adc9e2', 'black'), ('#d1c7e6', 'gray'), ('#b7d5f7', 'green'), ('#cdcce0', 'yellow'), ('#efefef', 'maroon'), ('#ced8e4', 'blue'), ('#e0edf1', 'silver'), ('#c1e3ff', 'fuchsia'), ('#eaf3fd', 'red')], default='', max_length=30),
        ),
    ]
