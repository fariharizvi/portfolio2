from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    contactno = models.CharField(max_length=15, blank=False, null=False)  # added contact number
    description = models.CharField(max_length=200, blank=True, null=True)
    photo = models.ImageField(upload_to='student_photos/', blank=False, null=False)


    def __str__(self):
        return self.name  # Shows name in admin panel


