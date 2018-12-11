from django.contrib import admin

# Register your models here.
from .models import Post
#from post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=['title','publishingDate','slug']
    list_display_links=['publishingDate']
    list_filter=['title']
    search_fields=['title','content']
    list_editable=['title']

    class Meta:
        model=Post

admin.site.register(Post,PostAdmin)
