# Generated by Django 3.0.6 on 2021-09-22 14:54

import authentication.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('range_type', models.CharField(choices=[('customer fee for withdrawal', 'Customer Fee For Withdrawal'), ('pos fee for withdrawal', 'Pos Fee For Withdrawal'), ('pos fee for transfer', 'Pos Fee For Transfer')], max_length=205)),
                ('user', models.ForeignKey(default=authentication.models.User, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Range',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_value', models.IntegerField()),
                ('max_value', models.IntegerField()),
                ('charge_amount', models.IntegerField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rangeCategory.Category')),
                ('user', models.ForeignKey(default=authentication.models.User, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
