# Generated by Django 2.0.2 on 2018-05-04 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_auto_20180503_2133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='decription',
            new_name='description',
        ),
    ]