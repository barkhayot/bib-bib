from django.shortcuts import render, get_object_or_404, redirect
from .models import Drive
from accounts.models import UserProfile
from .forms import PostDriveForm
import datetime
from django.db.models import Q
from .filters import DriveSearchForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator




# Get All Drives View

def GetDrives(request):
    current_time = datetime.datetime.now().date()
    #user = get_object_or_404(UserProfile, user=request.user)
    drive = Drive.objects.all().filter(date__gte=current_time).order_by('-created_at')[:5]
    myFilter = DriveSearchForm(request.GET, queryset=drive)
    drive = myFilter.qs
    coder = request.user
    
    context = {
        'drives' : drive,
        #'user' : user,
        'filter' : myFilter,
        'coder' : coder,
        
    }
    return render(request, 'drives/getdrives.html', context)

# Get Drive Detail View

def DriveDetail(request, pk):
    coder = request.user
    drive = get_object_or_404(Drive, pk=pk)
    profile = get_object_or_404(UserProfile, pk=drive.driver.pk)
    #user = get_object_or_404(UserProfile, user=request.user)
    context = {
        'drive': drive,
        'profile': profile,
        #'user' : user,
        'coder' : coder
    }
    return render(request, 'drives/drivedetail.html', context)

# Get Drive Delete View

@login_required(login_url='login')
def DriveDelete(request, pk):
    drive = get_object_or_404(Drive, pk=pk, driver=request.user)
    coder = request.user
    #profile = get_object_or_404(UserProfile, pk=drive.driver.pk)
    #user = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'POST':
        drive.delete()
        return redirect('GetDrives')
    context = {
        'drive': drive,
        'coder': coder
    }
    return render(request, 'drives/deletedrive.html', context)


# Post Drive View

@login_required(login_url='login')
def PostDrive(request):
    coder = request.user
    user = get_object_or_404(UserProfile, user=request.user)
    form = PostDriveForm()
    if request.method == 'POST':
        form = PostDriveForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.driver = request.user
            data.save()
            return redirect('GetDrives')
    context = {
        'form': form,
        'user': user,
        'coder': coder
    }
    return render(request, 'drives/postdrive.html', context)


# User <-- Drive Posts

@login_required(login_url='login')
def UserDrivePosts(request):
    coder = request.user
    user = get_object_or_404(UserProfile, user=request.user)
    drive = Drive.objects.all().filter(driver=request.user).order_by('-created_at')
    context = {
        'drives': drive,
        'user': user,
        'coder': coder
    }   
    return render(request, 'drives/userdrivepost.html', context)


# Search Drive View

def search(request):
    coder = request.user
    current_time = datetime.datetime.now().date()
    drive = Drive.objects.all().filter(date__gte=current_time).order_by('-created_at')
    myFilter = DriveSearchForm(request.GET, queryset=drive)
    drive = myFilter.qs
    paginator = Paginator(drive, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'coder' : coder,
        'drives' : drive,
        'filter' : myFilter,
        'page_obj': page_obj
    } 

    return render(request, 'drives/searchdrives.html', context)



def handle_not_found(request, exception):
    return render(request, '404.html', status=404)