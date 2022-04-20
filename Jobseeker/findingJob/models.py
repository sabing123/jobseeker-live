from django.db import models
from django.contrib.auth.models import User
from .validators import validate_file_extension


# Create your models here.

class JobCategory(models.Model):
    name = models.CharField(max_length=200, null=True)
    category_logo = models.ImageField(upload_to="category_logo", default="defaultlogo.png",
                                      validators=[validate_file_extension], null=True, blank=True)

    def __str__(self):
        return self.name


class jobdetail(models.Model):
    jobNature = (
        ('Part Time', 'Part Time'),
        ('Full Time', 'Full Time'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    location = models.CharField(max_length=200, null=True)
    type = models.CharField(max_length=200, null=True, choices=jobNature)
    salary = models.FloatField(max_length=200, null=True)
    description = models.TextField()
    responsibility = models.TextField()
    qualification = models.TextField()
    published_date = models.DateField(max_length=200, null=True)
    deadline_date = models.DateField(max_length=200, null=True)
    no_of_vaccinies = models.CharField(max_length=200, null=True)
    company_details = models.TextField()
    company_logo = models.ImageField(upload_to="company_logo", default="defaultlogo.png", null=True, blank=True)
    jobcategory = models.ForeignKey(JobCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name
