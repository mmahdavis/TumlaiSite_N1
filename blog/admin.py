from django.contrib import admin
from .models import *


class CategoryInline(admin.TabularInline):
    model = PostConnectToCategory
    extra = 1


class TagInline(admin.TabularInline):
    model = PostConnectToTag
    extra = 1


class CategoryAdmin(admin.ModelAdmin):
    inlines = (CategoryInline, TagInline,)


# Register your models here.
admin.site.register(Post, CategoryAdmin)
admin.site.register(PostComment)
admin.site.register(Tag)
admin.site.register(Category)
