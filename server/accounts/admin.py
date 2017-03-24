"""Account admin module."""
from django.contrib import admin

from accounts.models import AppUser


class AppUserAdmin(admin.ModelAdmin):
    """AppUser admin class."""

    fields = (
        'id',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_verified',
        'is_admin',
        'timestamp_subscription',
        'timestamp_modified'
    )
    readonly_fields = ('id', 'timestamp_subscription', 'timestamp_modified')
    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_verified',
        'is_admin'
    )

admin.site.register(AppUser, AppUserAdmin)
