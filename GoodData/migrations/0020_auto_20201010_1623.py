# Generated by Django 3.1.1 on 2020-10-10 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0019_project_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_detail',
            name='file_ID',
        ),
        migrations.RemoveField(
            model_name='project_detail',
            name='filename',
        ),
        migrations.RemoveField(
            model_name='project_detail',
            name='filepath',
        ),
        migrations.RemoveField(
            model_name='project_detail',
            name='filesize',
        ),
        migrations.RemoveField(
            model_name='project_detail',
            name='real_filename',
        ),
        migrations.AddField(
            model_name='project_detail',
            name='video',
            field=models.FileField(default=1, upload_to='media/project_video'),
            preserve_default=False,
        ),
    ]