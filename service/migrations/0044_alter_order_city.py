# Generated by Django 4.0.6 on 2022-10-23 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0043_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
