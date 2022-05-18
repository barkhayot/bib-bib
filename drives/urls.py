from django.urls import path
from . import views

urlpatterns = [
    path('', views.GetDrives, name="GetDrives"),
    path('post', views.PostDrive, name="PostDrive"),
    path('<int:pk>', views.DriveDetail, name="DriveDetail"),
    path('<int:pk>/delete', views.DriveDelete, name="DriveDelete"),
    path('mydrives', views.UserDrivePosts, name="UserDrivePosts"),
    path('search', views.search, name="SearchDrive")
]