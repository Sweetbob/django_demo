from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=32, default='title')
    content = models.TextField(null=True)
    post_date = models.DateField(null=True)


    # this method is like tostring from java
    def __str__(self):
        return self.title
