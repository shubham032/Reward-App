from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('upload_screenshot/<int:app_id>/', views.upload_screenshot, name='upload_screenshot'),
    path('profile/', views.profile, name='profile'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('add_app/', views.add_app, name='add_app'),
    path('edit_app/<int:app_id>/', views.edit_app, name='edit_app'),
    path('delete_app/<int:app_id>/', views.delete_app, name='delete_app'),
]

