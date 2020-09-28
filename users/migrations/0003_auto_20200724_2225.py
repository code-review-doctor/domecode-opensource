# Generated by Django 3.0.8 on 2020-07-24 16:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_profile_about"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="image",
            field=models.ImageField(
                default="default.jpg",
                null="True",
                upload_to="profile_pics/",
                validators=[
                    django.core.validators.validate_image_file_extension
                ],
            ),
        ),
    ]
