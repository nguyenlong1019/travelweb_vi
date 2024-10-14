from django.db import models
from travel_server.utils import CommonAbstract


class Contact(CommonAbstract):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    title = models.CharField(max_length=255)
    content = models.TextField()


    class Meta:
        verbose_name = 'Liên hệ'
        verbose_name_plural = 'Liên hệ'
        db_table = 'contact'
    

    def __str__(self):
        return f"{self.id} - {self.email}"
