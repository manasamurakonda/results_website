from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length = 10,unique = True)
    name = models.CharField(max_length=100)
    maths = models.CharField(max_length = 1)
    uhv = models.CharField(max_length = 1)
    ai = models.CharField(max_length = 1)
    ads = models.CharField(max_length = 1)
    oop = models.CharField(max_length = 1)
    adlab = models.CharField(max_length = 1)
    ooplab = models.CharField(max_length = 1)
    python = models.CharField(max_length = 1)
    lifeskills = models.CharField(max_length = 3)
    res = models.CharField(max_length = 4)
    sgpa = models.FloatField()
    def __str__(self):
        return self.name


