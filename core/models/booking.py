from django.db import models 
from travel_server.utils import CommonAbstract 
from .tourist_destination import TouristDestination 
from .tour_service import TourService 


class Booking(CommonAbstract):
    '''Lưu thông tin đặt vé du lịch, người dùng không cần đăng nhập'''

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    tour = models.ForeignKey(TouristDestination, on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(TourService, on_delete=models.SET_NULL, null=True)
    
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)
    booking_date = models.DateField(auto_now_add=True)
    total_price = models.DecimalField(decimal_places=2, max_digits=18)
    payment_status = models.CharField(max_length=15, default='Pending')

    class Meta:
        verbose_name = 'Đặt lịch'
        verbose_name_plural = 'Đặt lịch'
        db_table = 'booking'

    
    def __str__(self):
        return f"{self.id} - {self.customer_name}"

