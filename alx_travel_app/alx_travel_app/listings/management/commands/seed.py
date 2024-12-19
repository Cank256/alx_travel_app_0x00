from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Seed the database with sample data"

    def handle(self, *args, **kwargs):
        # Create sample users
        user, _ = User.objects.get_or_create(username="host_user", email="host@example.com")
        user.set_password("password123")
        user.save()

        # Create sample listings
        sample_listings = [
            {"title": "Beach House", "description": "A beautiful house by the beach.", "price_per_night": 100.00, "location": "Miami", "host": user},
            {"title": "Mountain Cabin", "description": "Cozy cabin in the mountains.", "price_per_night": 150.00, "location": "Aspen", "host": user},
        ]

        for listing_data in sample_listings:
            Listing.objects.create(**listing_data)

        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))