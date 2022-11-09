# Generated by Django 4.0.6 on 2022-10-05 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_remove_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='Exp',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='aadhar',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='aadhar_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='city',
            field=models.CharField(choices=[('Ariyalur', 'Ariyalur'), ('Chennai', 'Chennai'), ('Coimbatore', 'Coimbatore'), ('Cuddalore', 'Cuddalore'), ('Dharmapuri', 'Dharmapuri'), ('Dindigul', 'Dindigul'), ('Erode', 'Erode'), ('Kanchipuram', 'Kanchipuram'), ('Kanyakumari', 'Kanyakumari'), ('Karur', 'Karur'), ('Krishnagiri', 'Krishnagiri'), ('Madurai', 'Madurai'), ('Nagapattinam', 'Nagapattinam'), ('Namakkal', 'Namakkal'), ('Nilgiris', 'Nilgiris'), ('Perambalur', 'Perambalur'), ('Pudukkottai', 'Pudukkotai'), ('Ramanathapuram', 'Ramanathapuram'), ('Salem', 'Salem'), ('Sivaganga', 'Sivaganga'), ('Thanjavur', 'Thanjavur'), ('Theni', 'Theni'), ('Thoothukudi (Tuticorin)', 'Thoothukudi (Tuticorin)'), ('Tiruchirappalli', 'Tiruchirappalli'), ('Tirunelveli', 'Tirunelveli'), ('Tiruppur', 'Tiruppur'), ('Tiruvallur', 'Tiruvallur'), ('Tiruvannamalai', 'Tiruvannamalai'), ('Tiruvarur', 'Tiruvarur'), ('Vellore', 'Vellore'), ('Viluppuram', 'Viluppuram'), ('Virudhunagar', 'Virudhunagar')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='dob',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='other_photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='employee',
            name='permanent_add',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='present_add',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='profession',
            field=models.CharField(choices=[('Cook', 'Cook'), ('Full-time Maid', 'Full-time Maid'), ('part-time Maid', 'part-time Maid'), ('Gardner', 'Gardner'), ('Driver', 'Driver'), ('Electrician', 'Electrician'), ('Plumber', 'plumber')], max_length=200, null=True),
        ),
    ]