from django.shortcuts import render, redirect 
from core.models.tourist_destination import TouristDestination 
from django.http import Http404 


def destination_view(request):
    '''Danh sách các điểm đến'''
    tours = TouristDestination.objects.order_by('-created_at')
    context = {}
    context['tours'] = tours
    return render(request, 'core/destinations.html', context, status=200)


def destination_detail_view(request, slug):
    '''Chi tiết điểm đến'''

    try:
        tour = TouristDestination.objects.get(slug=slug)
    except TouristDestination.DoesNotExist:
        raise Http404()

    return render(request, 'core/new-detail.html', {'tour': tour}, status=200) 
