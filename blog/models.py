from django.db import models
from django.db.models.fields import CharField


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


class Category(models.Model):
    title = models.CharField(max_length=75)
    post = models.ManyToManyField(
        Post,
        through='PostConnectToCategory',
        through_fields=('Category_id', 'post_id'),
    )

    def __str__(self):
        return "%s" % (self.title)


class Tag(models.Model):
    title = models.CharField(max_length=75)
    post = models.ManyToManyField(
        Post,
        through='PostConnectToTag',
        through_fields=('tag_id', 'post_id'),
    )

    def __str__(self):
        return "%s" % (self.title)


class PostComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    comment_date = models.DateField()
    content_text = models.TextField(max_length=300)
    parent_pk = models.IntegerField()
    publiched = models.BooleanField(default=False)


class CustomerComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=30)
    title = models.CharField(max_length=100)
    comment_date = models.DateField()
    content_text = models.TextField(max_length=300)
    parent_pk = models.IntegerField()
    publiched = models.BooleanField(default=False)


class PostConnectToTag(models.Model):
    class Meta:
        verbose_name='Tag'
        verbose_name_plural = 'Tag'

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)


class PostConnectToCategory(models.Model):
    class Meta:
        verbose_name='Category'
        verbose_name_plural = 'Category'

    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    Category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
