from django.contrib import admin
from .models import *


class PostsAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_display = ("title", "is_published", "created_at", "id")


admin.site.register(Posts, PostsAdmin)
