# Generated by Django 2.0.2 on 2018-05-06 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ogbuifyscrumy', '0006_auto_20180506_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=100),
        ),
    ]
