# Generated by Django 4.0.6 on 2022-09-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0012_delete_profession'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cust_name', models.CharField(max_length=200, null=True)),
                ('worker', models.CharField(max_length=200, null=True)),
                ('pincode', models.CharField(max_length=200, null=True)),
            ],
        ),
    ]
