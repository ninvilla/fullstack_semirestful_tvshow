# Generated by Django 2.2 on 2021-05-19 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow_app', '0003_auto_20210517_0233'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShowManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
    ]
