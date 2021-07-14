from django.db import models
from django.http import request
from django.contrib.auth.models import User

# Create your models here.
class Poll(models.Model):
    user = models.CharField(max_length=100)
    question = models.TextField()
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)

    def total(self):
        return self.option_one_count + self.option_two_count
    def __str__(self):
        return self.user

class User(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    fname= models.CharField(max_length=100)
    lname= models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.fname + self.lname
    
    