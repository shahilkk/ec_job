# Generated by Django 4.0 on 2022-03-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_userdetails_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='profilePic',
            field=models.ImageField(default='User_images/', upload_to='User_images/'),
        ),
    ]
