# Generated by Django 2.0.2 on 2018-05-04 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_auto_20180503_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='room1',
            new_name='First_Room_Choice',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='ucs_time_date1',
            new_name='First_Time_Day_Choice',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='room2',
            new_name='Second_Room_Choice',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='ucs_time_date2',
            new_name='Second_Time_Day_Choice',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='room3',
            new_name='Third_Room_Choice',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='ucs_time_date3',
            new_name='Third_Time_Day_Choice',
        ),
    ]