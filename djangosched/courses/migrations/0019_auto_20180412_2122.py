# Generated by Django 2.0.3 on 2018-04-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0018_course_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.CharField(choices=[('Anthropology', 'Anthropology'), ('Art', 'Art'), ('Art History', 'Art History'), ('Biology', 'Biology'), ('Chemistry', 'Chemistry'), ('Computer Science', 'Computer Science'), ('Economics', 'Economics'), ('Environmental Studies', 'Environmental Studies'), ('Gender Studies', 'Gender Studies'), ('Geography', 'Geography'), ('History', 'History'), ('Interdivisional', 'Interdivisional'), ('Languages', 'Languages'), ('Literature', 'Literature'), ('Mathematics', 'Mathematics'), ('Music', 'Music'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Political Science', 'Political Science'), ('Psychology', 'Psychology'), ('Religion', 'Religion'), ('Sociology', 'Sociology'), ('Statistics', 'Statistics'), ('Theater', 'Theater'), ('Writing', 'Writing')], max_length=30),
        ),
    ]
