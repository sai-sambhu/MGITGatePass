# Generated by Django 2.2.5 on 2019-12-17 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0003_auto_20191217_0001'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentprofileinfo',
            name='jlt',
        ),
        migrations.AlterField(
            model_name='studentprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='profile_pics_students'),
        ),
    ]
