from django.contrib import admin
from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "created_at",
        "updated_at",
    )
    list_filter = ("created_at", "updated_at", "author")
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
