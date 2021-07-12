# Generated by Django 3.1.1 on 2020-10-06 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0005_auto_20201006_1332'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/orig')),
                ('filtered_image', models.ImageField(upload_to='uploads/%Y/%m/%d/filtered')),
                ('content', models.TextField(blank=True, max_length=500, null=True)),
                ('input_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
