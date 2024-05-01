from django.db import models
from django.contrib.auth import get_user_model


class Subjects(models.Model):
    student = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    attended = models.BooleanField(default=True)
    date = models.DateField()
    subject = models.CharField(max_length=200)
    band_score = models.IntegerField()
    teacher_review = models.TextField()

    def __str__(self):
        return self.subject