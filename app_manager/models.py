from django.db import models
from django.contrib.auth.models import User


class App(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    category = models.CharField(max_length=100)
    sub_category = models.CharField(max_length=100)
    points = models.IntegerField(default=0)
    icon = models.ImageField(upload_to='app_icons/', blank=True, null=True)  # Store in /media/app_icons/

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)  # Store in /media/profile_pictures/
    points_earned = models.IntegerField(default=0)
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class TaskCompletion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='task_screenshots/')  # Stores inside /media/task_screenshots/
    completed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.app.name}"

