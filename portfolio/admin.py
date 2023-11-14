from django.contrib import admin
from django.utils.html import format_html

from .models import Customer, Review, Reservation, Menu


class CustomerList(admin.ModelAdmin):
    list_display = ('pk', 'cust_number', 'name', 'city', 'cell_phone', 'agent')
    list_filter = ('cust_number', 'name', 'city', 'agent')
    search_fields = ('cust_number', 'name', 'agent')
    ordering = ['cust_number']


class ReviewList(admin.ModelAdmin):
    list_display = ('customer', 'menu_item', 'rating', 'name', 'description', 'meal_price')
    list_filter = ('customer', 'menu_item', 'rating', 'name')
    search_fields = ('customer', 'menu_item', 'rating', 'name')
    ordering = ['customer']


class ReservationList(admin.ModelAdmin):
    list_display = ('customer', 'name', 'number_of_guests', 'Booking_time')
    list_filter = ('customer', 'name', 'Booking_time')
    search_fields = ('customer', 'name', 'Booking_time')
    ordering = ['customer']


class MenuList(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'type',)  # Fields you want to show in the admin list view
    list_filter = ('type',)  # Add filtering by type (food/drink)
    search_fields = ('name', 'description',)  # Add search functionality for name and description
    ordering = ('name',)  # Order menu items by name in the admin list view

    # If you want to display the image in the admin, you can use this:
    # However, it's optional and only for visual purposes in the Django admin.
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px;" />', obj.image.url)
        return 'No Image'

    image_tag.short_description = 'Image'

    readonly_fields = ('image_tag',)  # Make the image_tag field read-only


admin.site.register(Customer, CustomerList)
admin.site.register(Review, ReviewList)
admin.site.register(Reservation, ReservationList)
admin.site.register(Menu, MenuList)