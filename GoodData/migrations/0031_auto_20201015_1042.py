# Generated by Django 3.1.1 on 2020-10-15 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0030_auto_20201014_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_detail',
            name='video',
            field=models.FileField(upload_to='static/project_video/'),
        ),
    ]
