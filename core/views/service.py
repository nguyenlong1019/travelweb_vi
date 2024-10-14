from django.shortcuts import render, redirect 
from core.models.tour_service import * 


def services_view(request):
    services = TourService.objects.order_by('-created_at')
    return render(request, 'core/restaurants.html', {'services': services}, status=200)


def service_detail_view(request):
    return render()
