# Generated by Django 3.1.1 on 2020-09-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20200913_0240'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='user_name',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
