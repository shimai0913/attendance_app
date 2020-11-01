# Generated by Django 3.1.2 on 2020-10-25 17:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendances', '0007_remove_attendance_attendance_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
    ]