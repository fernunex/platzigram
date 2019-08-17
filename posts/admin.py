from django.contrib import admin
from posts.models import Posts
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

@admin.register(Posts)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin Model"""

    list_display = ('pk','user','photo')
    list_display_links = ('pk','user')
    list_editable = ('photo',)
    list_filter = (
        'created',
        'modified',
        'user'
    )