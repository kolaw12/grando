from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(RoomAmenities)
admin.site.register(ContactForm)
admin.site.register(Booking)