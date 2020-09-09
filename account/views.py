from django.shortcuts import render, redirect
from .models import Profile


def profile(request):
    person = Profile.objects.all()
    context = {'person': person}
    return render(request, 'account/profile.html', context)
