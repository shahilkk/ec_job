# Generated by Django 3.2.9 on 2022-03-11 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_rename_login_userdetails_userlogin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workerdetails',
            old_name='address',
            new_name='w_address',
        ),
        migrations.RenameField(
            model_name='workerdetails',
            old_name='email',
            new_name='w_email',
        ),
        migrations.RenameField(
            model_name='workerdetails',
            old_name='phone',
            new_name='w_phone',
        ),
        migrations.RenameField(
            model_name='workerdetails',
            old_name='pincode',
            new_name='w_pincode',
        ),
        migrations.RenameField(
            model_name='workerdetails',
            old_name='profilePic',
            new_name='w_profilePic',
        ),
    ]