# Generated by Django 4.0.6 on 2022-10-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0041_order_ord_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=200),
        ),
    ]
