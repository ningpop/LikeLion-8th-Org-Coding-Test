from django.db import models
from home.models import Lecture
from django.contrib.auth.models import User

# Create your models here.

class LectureRequest(models.Model):
    title = models.CharField(max_length=100)
    professor = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # many to one field.
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title