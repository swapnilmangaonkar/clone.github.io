# Generated by Django 2.0.6 on 2018-06-03 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20180603_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]