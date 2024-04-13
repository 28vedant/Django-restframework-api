from django.db import models

# Create your models here.
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    about = models.TextField()
    type = models.CharField(max_length=255,choices=(('IT','IT'),
                                                    ('Financial','Financial'),
                                                    ('Banking','Banking')))
    added_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name + " ("+self.location+")"


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=255,choices=(('Manager','Manager'),
                                                        ('Developer','Developer'),
                                                        ('Tester','Tester')))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
   
