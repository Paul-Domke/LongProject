
# Generated by Django 2.0.2 on 2018-05-02 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0020_course_enemies'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='Class_Size',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
