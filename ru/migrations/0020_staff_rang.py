# Generated by Django 2.0.5 on 2018-08-04 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ru', '0019_research_little'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='rang',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
