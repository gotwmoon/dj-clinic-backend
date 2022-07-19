from django.contrib import admin
from .models import Post, Category

class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '__empty__'
    list_display = ('title', 'status', 'published_date', 'created_date')
    list_filter = ['status', 'published_date']
    search_fields = ['title', 'content']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
