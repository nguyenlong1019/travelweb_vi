from django.db import models 
from travel_server.utils import CommonAbstract 
from .tour_service import TourService 


class TransportRoute(CommonAbstract):
    '''Lưu thông tin toàn bộ chuyến đi gồm cả phương tiện di chuyển như tuyến tàu, xe hoặc chuyến bay'''
    
    VEHICLE = (
        ('Xe khách', 'Xe khách'),
        ('Máy bay', 'Máy bay'),
        ('Tàu hỏa', 'Tòa hỏa')
    )
    
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    departure = models.CharField(max_length=255, verbose_name='Điểm khởi hành')
    destination = models.CharField(max_length=255, verbose_name='Điểm đến')
    departure_time = models.DateField(auto_now_add=True, verbose_name='Ngày đi')
    arrival_time = models.DateField(auto_now_add=True, verbose_name='Ngày về')
    price = models.DecimalField(decimal_places=2, max_digits=18, null=True, blank=True, verbose_name='Giá vé')
    service_provider = models.ForeignKey(TourService, on_delete=models.SET_NULL, null=True, db_column='service_provider', verbose_name='Nhà cung cấp dịch vụ')
    vehicle = models.CharField(max_length=31, default='Xe khách', choices=VEHICLE, verbose_name='Loại hình di chuyển')
    amount = models.IntegerField(default=1, verbose_name='Số lượng người')
    quantity = models.IntegerField(default=10, verbose_name='Số vé còn')


    class Meta:
        verbose_name = 'Tour du lịch'
        verbose_name_plural = 'Tour du lịch'
        db_table = 'transport_route'

    
    def __str__(self):
        return f"{self.id}"


class Activity(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    transport_route = models.ForeignKey(TransportRoute, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Tên hoạt động', help_text='Các hoạt động như ăn uống, khách sạn, hướng dẫn viên du lịch, vé vui chơi, ...')
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')


    class Meta:
        verbose_name = 'Hoạt động trong tour'
        verbose_name_plural = 'Hoạt động trong tour'
        db_table = 'activities'

    
    def __str__(self):
        return f"{self.id} - {self.name}"
