# Generated by Django 5.1.6 on 2025-02-18 23:46

import login_system.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_system', '0003_alter_userprofile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(upload_to=login_system.models.user_directory_path),
        ),
    ]
