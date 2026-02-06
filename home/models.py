from django.db import models

# Create your models here.
class employee(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 122)
    department = models.CharField(max_length = 122)
    position = models.CharField(max_length = 122)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    hire_date = models.DateField()

    def __str__ (self):
       return self.name