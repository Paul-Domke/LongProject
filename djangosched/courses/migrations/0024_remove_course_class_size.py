# Generated by Django 2.0.3 on 2018-05-03 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0023_merge_20180503_1034'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='Class_Size',
        ),
    ]
