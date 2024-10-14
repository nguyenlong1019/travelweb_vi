from django.db import models 
from travel_server.utils import CommonAbstract 
from .tour_service import TourService 


class TransportRoute(CommonAbstract):
    '''Lưu thông tin tuyến tàu, xe hoặc chuyến bay'''
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    departure = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    departure_time = models.DateTimeField(auto_now_add=True)
    arrival_time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(decimal_places=2, max_digits=18, null=True, blank=True)
    service_provider = models.ForeignKey(TourService, on_delete=models.SET_NULL, null=True, db_column='service_provider')
    

    class Meta:
        verbose_name = 'Lộ trình'
        verbose_name_plural = 'Lộ trình'
        db_table = 'transport_route'

    
    def __str__(self):
        return f"{self.id}"

