# Generated by Django 4.0.6 on 2022-10-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0054_alter_employee_city'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cust_uid',
        ),
        migrations.RemoveField(
            model_name='order',
            name='uid',
        ),
        migrations.AddField(
            model_name='order',
            name='custname',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='emp_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='city',
            field=models.CharField(choices=[('Ariyalur', 'Ariyalur'), ('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'), ('Cuddalore', 'Cuddalore'), ('Dharmapuri', 'Dharmapuri'), ('Dindigul', 'Dindigul'), ('Erode', 'Erode'), ('Kanchipuram', 'Kanchipuram'), ('Kanyakumari', 'Kanyakumari'), ('Karur', 'Karur'), ('Krishnagiri', 'Krishnagiri'), ('Madurai', 'Madurai'), ('Nagapattinam', 'Nagapattinam'), ('Namakkal', 'Namakkal'), ('Nilgiris', 'Nilgiris'), ('Perambalur', 'Perambalur'), ('Pudukkottai', 'Pudukkotai'), ('Ramanathapuram', 'Ramanathapuram'), ('Salem', 'Salem'), ('Sivaganga', 'Sivaganga'), ('Thanjavur', 'Thanjavur'), ('Theni', 'Theni'), ('Thoothukudi (Tuticorin)', 'Thoothukudi (Tuticorin)'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Tirunelveli', 'Tirunelveli'), ('Tiruppur', 'Tiruppur'), ('Tiruvallur', 'Tiruvallur'), ('Tiruvannamalai', 'Tiruvannamalai'), ('Tiruvarur', 'Tiruvarur'), ('Vellore', 'Vellore'), ('Viluppuram', 'Viluppuram'), ('Virudhunagar', 'Virudhunagar')], max_length=200, null=True),
        ),
    ]
