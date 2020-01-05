# Generated by Django 2.2.9 on 2020-01-02 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sign_name', models.CharField(max_length=20)),
                ('sign_email', models.CharField(max_length=40)),
                ('identity', models.CharField(max_length=20)),
                ('sign_password', models.CharField(max_length=20)),
                ('sign_confirm_password', models.CharField(max_length=20)),
                ('signup_date', models.DateTimeField(verbose_name='date signed up')),
            ],
        ),
    ]