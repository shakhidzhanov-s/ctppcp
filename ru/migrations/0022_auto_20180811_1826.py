# Generated by Django 2.0.5 on 2018-08-11 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0021_auto_20180811_1523'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SummerSchool',
        ),
        migrations.RemoveField(
            model_name='event',
            name='rid',
        ),
        migrations.AlterField(
            model_name='document',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
