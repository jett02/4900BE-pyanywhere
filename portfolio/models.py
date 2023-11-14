from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Customer(models.Model):
    agent = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    cust_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    email = models.EmailField(max_length=200)
    cell_phone = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_number)

class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='review')
    menu_item = models.CharField(max_length=25, null=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250, null=True)
    meal_price = models.DecimalField(max_digits=10, decimal_places=2)
    visited_date = models.DateField(default=timezone.now, blank=True, null=True)

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def cust_number(self):
        return self.customer.cust_number


class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='reservations')
    reserve_time = models.TimeField(null=True),
    name = models.CharField(max_length=50)
    number_of_guests = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(6)], null=True)
    Booking_time = models.DateTimeField(null=False, blank=False, unique=True)

    def str(self):
        return self.name

    def created(self):
        self.recent_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.customer)

    def cust_number(self):
        return self.customer.cust_number


class Menu(models.Model):
    ITEM_CHOICES = (
        ('food', 'Food'),
        ('drink', 'Drink'),
    )

    name = models.CharField(max_length=255, verbose_name="Menu Item Name")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name="Price")
    type = models.CharField(max_length=10, choices=ITEM_CHOICES, default='food', verbose_name="Type of Item")
    image = models.ImageField(upload_to='menu_images/', null=True, blank=True, verbose_name="Image of the Item")

    def __str__(self):
        return self.name
