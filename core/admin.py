from django.contrib import admin
from core.models.tourist_destination import TouristDestination 
from core.models.tour_service import TourService 
from core.models.booking import Booking
from core.models.transport_route import TransportRoute, Activity
from core.models.payment import Payment 
from core.models.contact import Contact


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


class ActivityInline(admin.TabularInline):
    model = Activity 
    extra = 4


@admin.register(TransportRoute)
class TransportRouteAdmin(admin.ModelAdmin):
    search_fields = ['departure', 'destination']
    readonly_fields = ['created_at',]
    inlines = [ActivityInline]


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    search_fields = ['amount', 'payment_method', 'payment_status']
    readonly_fields = ['created_at',]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email', 'phone', 'title']
    readonly_fields = ['created_at',]
