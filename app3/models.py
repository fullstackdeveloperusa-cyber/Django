from django.db import models

# Create your models here.

class Computer(models.Model):
    cno=models.IntegerField()
    cname=models.CharField(max_length=100)
    ctype=models.CharField(max_length=50)
def __str__(self):
    return 'Computer all Objects with cno : +str(self.cno)'