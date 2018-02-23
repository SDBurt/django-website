from django.contrib import admin
from .models import Article


class PostModelAdmin(admin.ModelAdmin):
    """Admin Model, changed list, filter, and search"""
    list_display = ["title", "created", "updated"]
    list_filter = ["updated", "created"]
    search_fields = ["title", "content"]

    class Meta:
        """Class Model Meta"""
        model = Article




# Register new model
admin.site.register(Article, PostModelAdmin)
