# Generated by Django 2.0.6 on 2018-06-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180611_2001'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaOauth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=255)),
                ('expires_in', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MpesaPayment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=30)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
