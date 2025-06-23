from django.db import models
from django.utils.text import slugify
from users.models import User

class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=25, unique=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.name)
        self.slug = base_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=260, unique=True)
    details = models.TextField()
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        base_slug = slugify(self.title)

        count = 1
        while Article.objects.filter(slug=base_slug).exists():
            base_slug = f"{base_slug}-{count}"
            count += 1

        self.slug = base_slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

