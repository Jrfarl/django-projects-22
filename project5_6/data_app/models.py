from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    academic_class=models.CharField(max_length=50)
    major=models.CharField(max_length=50)
    gpa=models.FloatField()
    profile_pic=models.ImageField(upload_to='data_app/media/images', null=True, blank='true')

    def __str__(self):
        return self.name
        