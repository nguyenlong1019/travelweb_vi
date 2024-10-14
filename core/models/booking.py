from django.db import models 
from travel_server.utils import CommonAbstract 
from .tourist_destination import TouristDestination 
from .transport_route import TransportRoute  


class Booking(CommonAbstract):
    '''Lưu thông tin đặt vé du lịch, người dùng không cần đăng nhập'''

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tour = models.ForeignKey(TouristDestination, on_delete=models.SET_NULL, null=True, verbose_name='Điểm đến du lịch')
    transport = models.ForeignKey(TransportRoute, on_delete=models.SET_NULL, null=True, verbose_name='Tour du lịch')
    
    customer_name = models.CharField(max_length=255, verbose_name='Tên khách hàng')
    phone_number = models.CharField(max_length=20, verbose_name='Số điện thoại')
    address = models.TextField(verbose_name='Địa chỉ')
    email = models.EmailField(max_length=255, null=True, blank=True, verbose_name='Email khách hàng')
    booking_date = models.DateField(auto_now_add=True, verbose_name='Ngày đặt')
    total_price = models.DecimalField(decimal_places=2, max_digits=18, verbose_name='Tổng tiền')
    payment_status = models.CharField(max_length=15, default='Pending', verbose_name='Trạng thái thanh toán')

    class Meta:
        verbose_name = 'Đặt lịch'
        verbose_name_plural = 'Đặt lịch'
        db_table = 'booking'

    
    def __str__(self):
        return f"{self.id} - {self.customer_name}"

