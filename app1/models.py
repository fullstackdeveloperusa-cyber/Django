from django.db import models

# Create your models here.

class School(models.Model):
    sno=models.IntegerField(default=100)
    sname=models.CharField(max_length=100)
    stype=models.CharField(max_length=100)
def __str__(self):
    return 'School Object with sno: ' +str(self.sno)