# Generated by Django 4.0 on 2022-03-03 10:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='city',
        ),
        migrations.RemoveField(
            model_name='quick_booking',
            name='place',
        ),
        migrations.AddField(
            model_name='login',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetails'),
        ),
        migrations.AlterField(
            model_name='quick_booking',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetails'),
        ),
        migrations.AlterField(
            model_name='review',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.userdetails'),
        ),
        migrations.DeleteModel(
            name='Package_Details',
        ),
    ]
