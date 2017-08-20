from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_date', "published", 'last_edited')
    list_filter = ('publish_date',)
    list_editable = ('published',)
    ordering = ('-publish_date', '-last_edited', 'published')