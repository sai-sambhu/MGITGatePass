# Generated by Django 2.2.5 on 2019-12-17 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0005_auto_20191217_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='GatepassRequests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll', models.CharField(max_length=10)),
                ('reason', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='InchargeProfileInfo',
        ),
        migrations.AlterField(
            model_name='studentprofileinfo',
            name='roll',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
