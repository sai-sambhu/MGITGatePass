# Generated by Django 2.2.5 on 2019-12-18 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0009_auto_20191218_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gatepassrequests',
            name='status',
            field=models.CharField(blank=True, choices=[('D', 'D'), ('R', 'R'), ('A', 'A'), ('O', 'O'), ('N', 'N')], max_length=3),
        ),
    ]
