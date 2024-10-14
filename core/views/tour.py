from django.shortcuts import render, redirect 


def tours_view(request):
    return render(request, 'core/hotels.html', status=200)
