# Generated by Django 4.0.6 on 2022-10-05 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0022_remove_order_date_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
    ]
