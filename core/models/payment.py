from django.db import models 
from travel_server.utils import CommonAbstract 
from .booking import Booking 


class Payment(CommonAbstract):
    '''Lưu thông tin thanh toán'''

    PAYMENT_METHOD = (
        (0, 'ATM'),
        (1, 'Cash'),
        (2, 'Internet Banking'),
    )

    PAYMENT_STATUS = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    )

    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=18, decimal_places=2)
    payment_method = models.IntegerField(default=0, choices=PAYMENT_METHOD)
    payment_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(max_length=15, default='Pending')
    

    class Meta:
        verbose_name = 'Thanh toán'
        verbose_name_plural = 'Thanh toán'
        db_table = 'payment'

    
    def __str__(self):
        return f"{self.id} - {self.payment_status}"

