from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length=10)
    lastname = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    address = models.TextField()
    age = models.IntegerField()
    

    class Meta:
        db_table = 'student'
