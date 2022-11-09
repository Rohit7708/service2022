# Generated by Django 4.0.6 on 2022-10-24 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0048_remove_order_ord_uid_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=200, null=True),
        ),
    ]
