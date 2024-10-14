from django.db import models 
from travel_server.utils import CommonAbstract


class TourService(CommonAbstract):
    '''Chứa thông tin các dịch vụ du lịch như công ty lữ hành, nhà xe, tuyến tàu, khách sạn'''

    SERVICE_TYPE = (
        (0, 'Nhà xe'),
        (1, 'Công ty du lịch'),
        (2, 'Tuyến tàu'),
        (3, 'Vé máy bay'),
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255, verbose_name='Tên dịch vụ')
    service_type = models.IntegerField(default=0, choices=SERVICE_TYPE, verbose_name='Loại dịch vụ')
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    price = models.DecimalField(decimal_places=2, max_digits=18, null=True, blank=True, verbose_name='Giá dịch vụ')
    contact_info = models.CharField(max_length=255, null=True, blank=True, verbose_name='Thông tin liên hệ')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Vị trí')


    class Meta:
        verbose_name = 'Dịch vụ du lịch'
        verbose_name_plural = 'Dịch vụ du lịch'
        db_table = 'tourist_service'

    
    def __str__(self):
        return f"{self.id} - {self.name}"

