# Generated by Django 4.0.6 on 2022-10-05 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0020_order_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
