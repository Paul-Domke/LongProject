# Generated by Django 2.0.2 on 2018-03-29 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_auto_20180329_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='room',
            field=models.CharField(choices=[('HNS 114', 'HNS 114'), ('HNS 108', 'HNS 108'), ('HNS 106', 'HNS 106'), ('HNS E167/168', 'HNS E167/168'), ('HNS E169', 'HNS E169'), ('HNS E170', 'HNS E170')], max_length=10),
        ),
        migrations.AlterField(
            model_name='course',
            name='ucs_time_date',
            field=models.CharField(choices=[('MWF8', 'MWF8'), ('MWF9', 'MWF9'), ('MWF10', 'MWF10'), ('MWF11', 'MWF11'), ('MR121', 'MR121'), ('MR23', 'MR23'), ('MR34', 'MR34'), ('MW78', 'MW78'), ('TR910', 'TR910'), ('TR1011', 'TR1011'), ('TF12', 'TF12'), ('TF45', 'TF45')], max_length=10),
        ),
    ]
