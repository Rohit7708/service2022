# Generated by Django 4.0.6 on 2022-09-24 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0007_workers_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professions', models.CharField(choices=[('Cook', 'Cook'), ('Full-time Maid', 'Full-time Maid'), ('part-time Maid', 'part-time Maid'), ('Gardner', 'Gardner'), ('Driver', 'Driver'), ('Electrician', 'Electrician'), ('Plumber', 'plumber')], max_length=200, null=True)),
            ],
        ),
    ]