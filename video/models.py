from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField
from ckeditor.fields import RichTextField

class Item(models.Model):
    title = models.CharField(max_length=255)
    video = EmbedVideoField()  # same like models.URLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title + ' | ' + str(self.author)