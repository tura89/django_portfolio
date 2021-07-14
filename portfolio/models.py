from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100, default='')
    description = models.CharField(max_length=250, default='')
    image = models.ImageField(upload_to='portfolio/images', default='')
    url = models.URLField(blank=True, default='')

    def __str__(self):
        return self.title
