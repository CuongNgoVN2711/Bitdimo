# Generated by Django 2.1.3 on 2018-12-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bitdimo', '0002_auto_20181201_1702'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpost',
            name='area',
        ),
        migrations.AlterField(
            model_name='userpostcomment',
            name='time_comment',
            field=models.DateTimeField(),
        ),
    ]
