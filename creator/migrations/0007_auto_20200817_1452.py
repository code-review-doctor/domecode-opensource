# Generated by Django 3.1 on 2020-08-17 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0006_auto_20200817_1417'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='documentation_Devs',
            new_name='documentation_Devs_Link',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='documentation_Users',
            new_name='documentation_Users_Link',
        ),
    ]