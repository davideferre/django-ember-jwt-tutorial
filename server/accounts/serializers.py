"""Accounts serializers module."""
from rest_framework import serializers
from accounts.models import AppUser


class AppUserSerializer(serializers.ModelSerializer):
    """AppUser serializer class."""

    class Meta:
        model = AppUser
        fields = (
            'id',
            'email',
            'password',
            'first_name',
            'last_name',
            'is_active',
            'is_verified',
            'is_admin',
            'timestamp_subscription',
            'timestamp_modified'
        )
        write_only_fields = ('password',)
        read_only_fields = ('is_active', 'is_verified', 'is_admin', 'timestamp_subscription', 'timestamp_modified')

    def update(self, instance, validated_data):
        """Update user method."""
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance

    def create(self, validated_data):
        """Create user method."""
        instance = AppUser.objects.create_user(**validated_data)
        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance
