# Generated by Django 3.1.1 on 2020-11-02 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GoodData', '0050_auto_20201030_1400'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('notice_id', models.AutoField(primary_key=True, serialize=False)),
                ('notice_title', models.CharField(max_length=100)),
                ('notice_content', models.TextField()),
                ('notice_inputer', models.CharField(max_length=50)),
                ('input_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
