from django.db import models

class MyNews(models.Model):
    new = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='static/main', blank=True)
    text = models.TextField()
    data = models.DateTimeField()

    def __str__(self):
        return f'{self.new.title()}'
