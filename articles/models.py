from django.db import models

# Create your models here.
class Article(models.Model):
    def __str__(self):
        return self.title
    title = models.CharField(max_length=200, null=False)
    content = models.TextField(null=True)