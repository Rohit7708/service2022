# Generated by Django 4.0.6 on 2022-10-05 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0021_alter_order_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date_created',
        ),
    ]
