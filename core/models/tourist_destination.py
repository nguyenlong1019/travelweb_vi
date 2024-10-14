from django.db import models 
from travel_server.utils import CommonAbstract


class TouristDestination(CommonAbstract):
    '''Chứa thông tin về các địa điểm du lịch trên toàn quốc'''
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Tên địa điểm')
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Vị trí, tỉnh thành')
    image = models.ImageField(upload_to='tour_dest_images/', null=True, blank=True, verbose_name='Ảnh')
    best_season = models.CharField(max_length=100, null=True, blank=True, verbose_name='Mùa đẹp nhất để du lịch')


    class Meta:
        verbose_name = 'Điểm đến du lịch'
        verbose_name_plural = 'Điểm đến du lịch'
        db_table = 'tourist_destination'

    
    def __str__(self):
        return f"{self.id} - {self.name}"

