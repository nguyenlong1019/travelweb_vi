from django.db import models 
from django.utils import timezone 


class CommonAbstract(models.Model):
    created_at = models.DateTimeField(editable=False, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        abstract = True 
        ordering = ('-created_at', )

    
    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()
        super(CommonAbstract, self).save(*args, **kwargs)
