# Generated by Django 3.1.1 on 2020-10-13 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0023_auto_20201013_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_detail',
            name='video',
            field=models.FileField(upload_to='project_video/'),
        ),
    ]
