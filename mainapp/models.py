from django.db import models
from django.urls import reverse
from django.conf import settings

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def clean(self):
        self.name = self.name.lower()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag_posts', args=[str(self.name)])
        
class BlogPost(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    body = models.TextField()
    postdate = models.DateTimeField(auto_now_add=True, blank=True)
    tags = models.ManyToManyField('Tag', related_name='posts')

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post', args=[str(self.id)])
