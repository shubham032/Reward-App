from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from .models import App, TaskCompletion, UserProfile
from .forms import ScreenshotUploadForm, UserProfileForm, AppForm

def home(request):
    return render(request, 'home.html')

@login_required
def admin_dashboard(request):
    """Only allow admins to access this page."""
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    
    if not user_profile.is_admin:
        return HttpResponseForbidden("You are not authorized to access this page.")
    
    apps = App.objects.all()
    return render(request, 'admin_dashboard.html', {'apps': apps})

@login_required
def add_app(request):
    """Allows admin to add a new app."""
    if request.method == "POST":
        form = AppForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AppForm()
    
    return render(request, 'add_app.html', {'form': form})

@login_required
def edit_app(request, app_id):
    """Allows admin to edit an existing app."""
    app = get_object_or_404(App, id=app_id)
    if request.method == "POST":
        form = AppForm(request.POST, request.FILES, instance=app)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
    else:
        form = AppForm(instance=app)

    return render(request, 'edit_app.html', {'form': form, 'app': app})

@login_required
def delete_app(request, app_id):
    """Allows admin to delete an app."""
    app = get_object_or_404(App, id=app_id)
    if request.method == "POST":
        app.delete()
        return redirect('admin_dashboard')

    return render(request, 'delete_app.html', {'app': app})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create the UserProfile instance with is_admin field
            is_admin = request.POST.get('is_admin') == 'on'
            UserProfile.objects.get_or_create(user=user, defaults={'is_admin': is_admin})

            login(request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def user_logout(request):
    """Logs out the user and redirects to home."""
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request,'home.html') 

@login_required
def dashboard(request):
    apps = App.objects.all()
    completed_tasks = TaskCompletion.objects.filter(user=request.user)
    total_points = sum(task.app.points for task in completed_tasks)

    return render(request, 'dashboard.html', {
        'apps': apps,
        'completed_tasks': completed_tasks,
        'total_points': total_points
    })

@login_required
def upload_screenshot(request, app_id):
    app = get_object_or_404(App, id=app_id)
    if request.method == 'POST':
        form = ScreenshotUploadForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.app = app
            task.save()
            return redirect('dashboard')
    else:
        form = ScreenshotUploadForm()

    return render(request, 'upload_screenshot.html', {'form': form, 'app': app})

@login_required
def profile(request):
    profile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'profile.html', {'form': form, 'profile': profile})
