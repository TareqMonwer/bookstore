from django.shortcuts import render



def user_settings(request):
    return render(request, 'user_settings.html')