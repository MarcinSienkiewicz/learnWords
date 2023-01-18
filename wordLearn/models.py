from django.db import models

class Word(models.Model):
    english = models.CharField(max_length=100)
    part = models.CharField(max_length=20)
    eng_meaning = models.CharField(max_length=250)
    polish = models.CharField(max_length=310)

    def __str__(self):
        return f"{self.id} {self.english}"