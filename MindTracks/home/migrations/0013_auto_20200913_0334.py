# Generated by Django 3.1.1 on 2020-09-13 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_profile_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_name',
            field=models.CharField(default='john', max_length=200),
        ),
    ]
