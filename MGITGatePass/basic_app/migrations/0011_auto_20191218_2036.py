# Generated by Django 2.2.5 on 2019-12-18 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0010_auto_20191218_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepassrequests',
            name='status',
            field=models.CharField(blank=True, choices=[('Denied', 'Denied'), ('Requested', 'Requested'), ('Approved', 'Approved'), ('OutOfColloge', 'OutOfColloge'), ('NotRequested', 'NotRequested')], max_length=15),
        ),
    ]
