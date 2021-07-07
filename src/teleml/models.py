from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    avatar = models.ImageField(upload_to='avatars/', default='profile_icon.png')
    website = models.CharField(max_length=255, blank=True, null=True)


User.userprofile = property(lambda u:UserProfile.objects.get_or_create(user=u)[0])


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TeleModel(models.Model):
    title = models.CharField(max_length=125)
    description = models.TextField()
    logo = models.ImageField(upload_to='uploads/', default='model_icon.jpg')
    file = models.FileField(upload_to='files/')
    category = models.ForeignKey(Category, default=None, related_name='items', on_delete=models.CASCADE)
    version = models.FloatField()
    require_version = models.FloatField()
    downloads = models.IntegerField(default=0)
    created_by = models.ForeignKey(User, related_name='models', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ('-created_at',)

