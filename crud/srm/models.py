# import the standard Django Model
# from built-in library
from django.db import models

# Create your models here.
# declare a new model with a name "students"
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
   
]
# Create your models here.
class students(models.Model):
    student_number =models.IntegerField()
    first_name= models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    date_birth = models.DateField()
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=600)
    cgpa = models.FloatField(default=0)

    def __str__(self):
        return f"{self.student_number} {self.first_name} {self.last_name}"  