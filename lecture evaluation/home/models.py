from django.db import models

LECTURE_SCORE = [
    (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10),
]

# Create your models here.

class Lecture(models.Model):
    title = models.CharField(max_length=200)
    professor = models.CharField(max_length=20)
    #score = models.DecimalField(max_digits=2, decimal_places=1)
    
    def __str__(self):
        return self.title
    
class Review(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, null=True, blank=True, related_name='review')
    personal_score = models.CharField(max_length=3, choices=LECTURE_SCORE, default='None')
    body = models.TextField()

    def __str__(self):
        return self.body
    