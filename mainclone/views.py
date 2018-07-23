from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required(login_url='/accounts/login/')
def home(request):
    Profile.usercheck(request.user)
    return render(request, 'landing.html', locals())