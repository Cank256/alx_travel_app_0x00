from django.db import models
from django.contrib.auth.models import User

class Listing(models.Model):
    listing_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=255)
    host = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings")
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    booking_id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bookings")
    guest = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(
        max_length=10,
        choices=[("pending", "Pending"), ("confirmed", "Confirmed"), ("canceled", "Canceled")],
    )
    created_at = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="reviews")
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField()  # Assuming 1-5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)