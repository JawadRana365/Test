from django.db import models

# Create your models here.

class Teacher(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    profilePicture = models.FileField(upload_to='images/', null=True, verbose_name="")
    emailAddress = models.EmailField(max_length=254, unique=True)
    phoneNumber = models.CharField(max_length=50)

    def __str__(self):
        return self.lastName


class Subject(models.Model):
    teacherId = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="tosubject",default=1)
    roomNo = models.CharField(max_length=20)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name