from django.db import models 
from travel_server.utils import CommonAbstract 
from ckeditor_uploader.fields import RichTextUploadingField 


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
    slogan = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    detail = RichTextUploadingField(null=True, blank=True, verbose_name='Giới thiệu')
    image = models.ImageField(upload_to='service_logo/', null=True, blank=True, verbose_name='Logo')
    banner = models.ImageField(upload_to='service_banner/', null=True, blank=True, verbose_name='Banner')
    price = models.DecimalField(decimal_places=2, max_digits=18, null=True, blank=True, verbose_name='Giá dịch vụ từ')
    contact_info = models.CharField(max_length=255, null=True, blank=True, verbose_name='Thông tin liên hệ')
    hotline = models.CharField(max_length=20, null=True, blank=True, verbose_name='Hotline')
    email = models.EmailField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True, verbose_name='Địa chỉ')
    location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Vị trí')


    class Meta:
        verbose_name = 'Dịch vụ du lịch'
        verbose_name_plural = 'Dịch vụ du lịch'
        db_table = 'tourist_service'

    
    def __str__(self):
        return f"{self.id} - {self.name}"

