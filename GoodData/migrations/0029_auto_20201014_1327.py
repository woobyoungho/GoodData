# Generated by Django 3.1.1 on 2020-10-14 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0028_auto_20201014_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_detail',
            name='user1',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project_detail',
            name='user2',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project_detail',
            name='user3',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project_detail',
            name='user4',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='project_detail',
            name='user5',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
