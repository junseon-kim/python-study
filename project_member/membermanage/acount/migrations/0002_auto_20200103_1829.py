# Generated by Django 2.2.9 on 2020-01-03 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='identity',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='sign_confirm_password',
            new_name='confirm_password',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='sign_name',
            new_name='password',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='sign_email',
            new_name='useremail',
        ),
        migrations.RenameField(
            model_name='signup',
            old_name='sign_password',
            new_name='username',
        ),
    ]
