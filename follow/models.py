from django.db import models

# Create your models here.
class Student(models.Model):
	name = models.Charfields(max_length=20)
