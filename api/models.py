from django.db import models

# Create your models here.

#specifying choices
WORK = (
    ('Full Time', 'Full time'),
    ('Part Time','Part-time'),
    ('IT','IT'),
    ('Non IT','Non IT'),
    ('Mobile Phones','Mobile Phones')
)


PSN = (
    ('Manager','Manager'),
    ('Frotend','Frotend'),
    ('Backend','Backend'),
    ('Fullstack','Fullstack'),
)

#Creating Company Model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    types = models.CharField(max_length=50,choices = WORK)
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
#Creating Employee Model

class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=50,choices=PSN)
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
