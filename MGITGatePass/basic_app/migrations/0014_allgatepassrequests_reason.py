# Generated by Django 2.2.5 on 2019-12-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0013_allgatepassrequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='allgatepassrequests',
            name='reason',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]