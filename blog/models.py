from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name  
    


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Dratf'),
        ('published', 'Published')
    )

    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    auhtor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() # default manager
    postObjects = PostObjects() # custom manager 

    class Meta:
        ordering = ('-published', )

    def __str__(self) -> str:
        return self.title