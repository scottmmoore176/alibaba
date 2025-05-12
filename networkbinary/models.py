from django.db import models

# Create your models here.

class Ali(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    
class Ram(models.Model):
    email = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    
class Google(models.Model):
    email = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    
class Googlep(models.Model):
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.password
    
class Git(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username
