# Generated by Django 4.0.6 on 2022-10-06 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0025_delete_application'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='booked_cust',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='worker',
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
