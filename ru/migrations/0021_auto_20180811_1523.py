# Generated by Django 2.0.5 on 2018-08-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0020_staff_rang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='journal',
            field=models.CharField(max_length=100),
        ),
    ]
