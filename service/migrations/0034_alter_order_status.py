# Generated by Django 4.0.6 on 2022-10-12 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0033_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'ending'), ('Completed', 'Completed')], default='Pending', max_length=200, null=True),
        ),
    ]
