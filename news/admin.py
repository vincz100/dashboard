from django.contrib import admin
from .models import Category, Post, Comment

class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title", "post_date", "modification_date")
    list_display_links = ["modification_date"]
    list_filter = ["title", "modification_date"]
    list_editable = ["title"]

    search_fields = ["title", "author", "modification_date"]
    prepopulated_fields = {"slug": ("title", "author")}
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)