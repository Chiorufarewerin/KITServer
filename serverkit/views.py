from django.shortcuts import render


def home(request):
    return render(request, 'serverkit/home.html')