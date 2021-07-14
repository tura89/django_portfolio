from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/images', blank=True)
    date = models.DateField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
