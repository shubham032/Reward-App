from django import forms
from django.contrib.auth.models import User
from .models import TaskCompletion, UserProfile, App

class ScreenshotUploadForm(forms.ModelForm):
    class Meta:
        model = TaskCompletion
        fields = ['screenshot']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture']

class AppForm(forms.ModelForm):
    class Meta:
        model = App
        fields = ['name', 'link', 'category', 'sub_category', 'points', 'icon']