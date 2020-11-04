from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")
    

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")
    video_url = models.URLField(null=True, blank=True)
    file = models.URLField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    body = RichTextField(blank=True, null=True)
    #body = models.TextField(blank=True, null=True)
    post_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=255, default='Graphics Designing')
    likes = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def total_likes(self):
        return self.likes.count()


    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('blog-detail', args=[self.id,])
        return reverse('home')

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE,)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)



