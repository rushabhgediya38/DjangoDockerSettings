from django.db import models


class Post(models.Model):
    attachment = models.FileField()
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name