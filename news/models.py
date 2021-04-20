from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, null=False, blank=False)
    link = models.CharField(max_length=2048)
    author_name = models.CharField(max_length=255, null=False, blank=False)
    upvoted = models.IntegerField(default=0)
    created = models.DateField(editable=False, auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    authon_name = models.CharField(max_length=255, null=False, blank=False)
    content = models.TextField()
    created = models.DateField(editable=False, auto_now_add=True)

