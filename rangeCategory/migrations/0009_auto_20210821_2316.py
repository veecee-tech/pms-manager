# Generated by Django 3.0.6 on 2021-08-21 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rangeCategory', '0008_auto_20210821_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]