# Generated by Django 3.1.1 on 2020-10-13 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0021_auto_20201013_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_detail',
            name='video',
            field=models.ImageField(upload_to='static/project_video'),
        ),
    ]