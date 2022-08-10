from django.contrib import admin
from post.models import Post, Like


class PostAdmin(admin.ModelAdmin):

    def count_like(self, obj):
        return obj.likes.filter(like=True).count()

admin.site.register(Post, PostAdmin)
admin.site.register(Like)