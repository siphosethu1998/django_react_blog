from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=500)
    author = models.CharField(max_length=50)

    def __str__(self):
        return self.title
