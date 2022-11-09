# Generated by Django 4.0.6 on 2022-10-27 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0061_order_date_created_order_status_alter_order_domestic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=200, null=True),
        ),
    ]
