# Generated by Django 3.1.2 on 2020-11-04 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendances', '0012_auto_20201103_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='attendance_details_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Attendance Details ID'),
        ),
    ]
