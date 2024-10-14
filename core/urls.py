from django.urls import path 
from core.views.index import *
from core.views.destination import * 
from core.views.service import * 
from core.views.tour import * 


urlpatterns = [
    path('', index_view, name='index'),
    path('gioi-thieu/', about_view, name='about'),
    path('hoat-dong/', activities_view, name='activities'),
    path('diem-den/', destination_view, name='destinations'),
    path('lien-he/', contact_view, name='contact'),
    path('diem-den/<slug:slug>.html', destination_detail_view, name='destination-detail'),
    path('dich-vu/', services_view, name='services'),
    path('dat-tour/', tours_view, name='tours'),
]

