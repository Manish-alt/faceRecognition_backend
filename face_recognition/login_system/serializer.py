from django.contrib.auth.models import User
from login_system.models import UserProfile
from rest_framework import serializers
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    def get_image(self, obj):
        """Return the full URL of the image"""
        request = self.context.get('request')  # Get request from context
        if obj.image:
            return request.build_absolute_uri(obj.image.url) if request else f"{obj.image.url}"
        return None
    
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number', 'image', 'source', 'destination', 'current_balance', 'deducted_balance']