# Generated by Django 2.0.2 on 2018-05-06 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ogbuifyscrumy', '0007_auto_20180506_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]
