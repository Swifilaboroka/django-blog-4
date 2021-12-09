from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import related
from django.urls import reverse
from django.utils.text import slugify
from tinymce.models import HTMLField
import uuid


class Tag(models.Model):
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=60)
    description = models.TextField(max_length=200)
    content = HTMLField()
    slug = models.SlugField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='post_images')
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"slug": self.slug})
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) + "-" + str(self.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-timestamp',)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("post_list", kwargs={"pk": self.pk})
    

    def __str__(self):
        return self.name


