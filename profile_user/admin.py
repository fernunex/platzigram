""" User admin classes"""

#Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from profile_user.models import Profile
from django.contrib.auth.models import User

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """"PROFILE ADMIN"""
    list_display = (
    'pk',
    'user',
    'phone_number',
    'website',
    'picture')
    list_display_links = (
    'pk',
    'user',)
    list_editable= ('phone_number','website','picture')
    search_fields = (
    'user__email',
    'user__username',
    'user__first_name',
    'phone_number',
    'user__last_name'
    )

    list_filter = (
    'user__is_active',
    'user__is_staff',
    'created',
    'modified',
    )

    fieldsets = (
        ('Profile',{
            'fields':(('user','picture'),),
        }),
        ('Extra info',{
            'fields':(('phone_number','website'),
                        ('biography'),),
        }),
        ('Metadata',{
            'fields':(('created','modified'),),
        }),
        )

    readonly_fields = ('created','modified',)

class ProfileInline(admin.StackedInline):
    """"Profile in-line admin for user"""
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin sssss"""
    inlines = (ProfileInline,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        
    ) 

admin.site.unregister(User)
admin.site.register(User, UserAdmin)



