# Generated by Django 3.1 on 2022-02-20 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20220219_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_picture',
            field=models.ImageField(default='default_profile_pic.png', upload_to='userprofile'),
        ),
    ]