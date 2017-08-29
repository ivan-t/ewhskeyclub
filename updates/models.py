from django.db import models
from datetime import date

# Create your models here.
class Post(models.Model):
    title =  models.CharField(max_length=200)
    publish_date = models.DateField(default=date.today)
    content = models.TextField()
    last_edited = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_urls(self):
        return "/updates/%s/" %(self.id)

    class Meta:
        ordering = ["-publish_date", "-last_edited"]