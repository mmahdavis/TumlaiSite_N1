from django.db import models
from django.db.models.fields import CharField
from datetime import date


# Create your models here.

class CommentManager(models.Manager):
    def get_by_id(self, pk):
        qs = self.get_queryset().filter(parent_pk=pk)
        return qs


class Category(models.Model):
    title = models.CharField(max_length=75)

    # obj = CategoryManager()
    def __str__(self):
        return "%s" % (self.title)


class Tag(models.Model):
    title = models.CharField(max_length=75)

    def __str__(self):
        return "%s" % (self.title)


class Post(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=400)
    content_text = models.TextField(max_length=4500)
    data_date = models.DateField()
    author = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='blog/',
        height_field=None,
        width_field=None,
        max_length=100,
        )
    category = models.ManyToManyField("Category")
    tag = models.ManyToManyField("Tag")


class PostComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    title = models.CharField(max_length=100)
    comment_date = models.DateField(auto_now=True)
    content_text = models.TextField(max_length=300)
    parent_pk = models.IntegerField(null=True, default=-1)
    publiched = models.BooleanField(default=False)
    object = CommentManager

    def __str__(self):
        return str(self.post_id.id)

