from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(UserProfile)

class UserAdmin(admin.ModelAdmin):
    model = User
    field = ['first_name', 'last_name', 'email', 'phone_number', 'image', 'source', 'destination', 'current_balance', 'deducted_balance']

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
