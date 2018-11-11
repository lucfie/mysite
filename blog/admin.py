from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['post_title', 'post_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    list_display = ('post_title', 'post_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['post_title', 'post_text']


admin.site.register(Post, PostAdmin)

