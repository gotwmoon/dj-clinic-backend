from django.contrib import admin
from .models import Post, Category, Comment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
    date_hierarchy = 'created_date'
    empty_value_display = '__empty__'
    list_display = ('title', 'status', 'published_date', 'created_date')
    list_filter = ['status', 'published_date']
    search_fields = ['title', 'content']

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_values_display= "__empty__"
    list_display = ['name', 'post', 'approved', 'created_date']
    list_filter = ['approved', 'post']
    search_fields = ['name', 'post']    


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Comment, CommentAdmin)
