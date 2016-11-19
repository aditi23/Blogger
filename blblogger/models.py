import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Blog(models.Model):
    heading = models.CharField(max_length=200)
    post = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post

    def get_absolute_url(self):
        return reverse('create-blog')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)



