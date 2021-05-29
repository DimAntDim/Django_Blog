from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    # default manager
    objects = models.Manager()
    #  Custom manager returning only published Post's
    published = PublishedManager()

    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    # unique_for_date create slugs using posts publish date, preventing post with same slug
    slug = models.SlugField(max_length=250, unique_for_date='publish')  
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField(blank=True)
    publish = models.DateTimeField(default=timezone.now)
    # auto_now_add will save the date automatically when creating an object
    created = models.DateTimeField(auto_now_add=True)
    # auto_now will update automatically when saving an object
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ('-publish',)

        def __str__(self):
            return self.title
    
    def get_absolute_url(self):
        return reverse('blog: post_detail', args=[self.publish.year, self.publish.month, self.publish.day, self.slug])
