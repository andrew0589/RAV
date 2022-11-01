# Generated by Django 4.1.2 on 2022-10-10 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('driver_license', models.IntegerField()),
                ('drivers_validity_license', models.DateTimeField()),
                ('country_of_residence', models.CharField(max_length=30)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]