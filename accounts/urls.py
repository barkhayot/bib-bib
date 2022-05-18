from django.urls import path
from . import views

urlpatterns = [
    # Authentication
    path('register', views.RegisterUser, name='register'),
    path('login', views.LoginUser, name='login'),
    path('logout', views.LogoutUser, name='logout'),

    # User Profile
    path('profile', views.Profile, name='UserProfile'),
    path('profile/edit', views.EditProfile, name='EditProfile'),
    path('driver/<int:pk>', views.DriverProfile, name="DriverProfile")

]