from django.db import models

class Student(models.Model):
    name        = models.CharField(max_length = 100 , null = True , blank = True)
    phone       = models.CharField(max_length = 11 , null = True , blank = True)
    address     = models.CharField(max_length = 1000 , null = True , blank = True)

    def __str__(self):
        return self.name