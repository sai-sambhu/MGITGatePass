# Generated by Django 2.2.5 on 2019-12-16 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofileinfo',
            name='jlt',
            field=models.CharField(default='i am sai', max_length=5),
        ),
    ]
