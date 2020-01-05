from djongo import models


class signup(models.Model):
    username = models.CharField(max_length=20)
    identity = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=40)
    signup_date = models.DateTimeField('date signed up')


class login(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)



# Create your models here.
