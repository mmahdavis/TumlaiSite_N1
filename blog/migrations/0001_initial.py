# Generated by Django 3.2.8 on 2021-11-29 05:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(max_length=400)),
                ('content_text', models.TextField(max_length=4500)),
                ('data_date', models.DateField()),
                ('author', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='blog/')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('post', models.ManyToManyField(to='blog.Post')),
            ],
        ),
        migrations.CreateModel(
            name='PostComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('title', models.CharField(max_length=100)),
                ('comment_date', models.DateField(auto_now=True)),
                ('content_text', models.TextField(max_length=300)),
                ('parent_pk', models.IntegerField(default=-1, null=True)),
                ('publiched', models.BooleanField(default=False)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.post')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('post', models.ManyToManyField(to='blog.Post')),
            ],
        ),
    ]
