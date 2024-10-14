from django.contrib import admin
from core.models.tourist_destination import TouristDestination 
from core.models.tour_service import TourService 
from core.models.booking import Booking
from core.models.transport_route import TransportRoute 
from core.models.payment import Payment


@admin.register(TouristDestination)
class TouristDestinationAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location']
    readonly_fields = ['created_at',]


@admin.register(TourService)
class TourServiceAdmin(admin.ModelAdmin):
    search_fields = ['name', 'location']
    readonly_fields = ['created_at',]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    search_fields = ['customer_name', 'phone_number', 'address', 'email']
    readonly_fields = ['created_at',]


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    search_fields = ['departure', 'destination']
    readonly_fields = ['created_at',]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['amount', 'payment_method', 'payment_status']
    readonly_fields = ['created_at',]
