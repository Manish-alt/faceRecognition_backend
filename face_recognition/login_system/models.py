import uuid
from django.db import models
import os

def user_directory_path(instance, filename):
    """Generate file path with instance ID as the filename"""
    ext = filename.split('.')[-1]  # Get the file extension
    filename = f"{instance.pk}.{ext}" if instance.pk else filename  # Use instance ID if available
    return os.path.join('uploads/', filename)  # Save inside 'uploads/user_profile_images' folder

# Create your models here.
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True, default='')
    image = models.ImageField(upload_to=user_directory_path)
    source = models.CharField(max_length=100, blank=True, null=True, default='')
    destination = models.CharField(max_length=100, blank=True, null=True, default='')
    current_balance = models.FloatField(default=0.0)
    deducted_balance = models.FloatField(default=0.0)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
    
    def save(self, *args, **kwargs):
        """Save instance first to get an ID, then update the filename."""
        super().save(*args, **kwargs)  # Save to get ID
        if self.image:
            ext = self.image.name.split('.')[-1]  # Extract extension
            new_filename = f"uploads/{self.pk}.{ext}"  # New path
            if self.image.name != new_filename:
                os.rename(self.image.path, os.path.join('media', new_filename))
                self.image.name = new_filename  # Update name
                super().save(update_fields=['image'])  # Save again