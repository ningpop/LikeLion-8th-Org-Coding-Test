from django.db import models
from django.contrib.auth.models import User

LECTURE_SCORE = [
    ('★☆☆☆☆', '★☆☆☆☆'), ('★★☆☆☆', '★★☆☆☆'), ('★★★☆☆', '★★★☆☆'), ('★★★★☆', '★★★★☆'), ('★★★★★', '★★★★★'),
]

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=100)
    professor = models.CharField(max_length=20)
    #score = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # many to one field.
    created_at = models.DateField(auto_now=True)
    personal_score = models.CharField(max_length=10, choices=LECTURE_SCORE, default='None')
    body = models.TextField()

    class Meta:
        ordering = ['-id']

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.body
    