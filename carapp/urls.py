from django.urls import path
from carapp import views

app_name ="carapp"

urlpatterns = [
    path('', views.index, name = 'home_page'),
    path('about/',views.about, name = 'about_page'),
    path('amenity/',views.amenity, name = 'amenity_page'),
    path('booking/',views.booking, name = 'booking_page'),
    path('contact/',views.contact, name = 'contact_page'),
    path('event/',views.event, name = 'events_page'),
    path('gallery/',views.gallery, name = 'gallery_page'),
    path('location/',views.location, name = 'location_page'),
    path('offer/',views.offer, name = 'offer_page'),
    path('privacy/',views.privacy, name = 'privacy_page'),
    path('restaurant/',views.restaurant, name = 'restaurant_page'),
    path('details/<str:room_id>/',views.room_details, name = 'room_details'),
    path('rooms/',views.rooms, name = 'room_page'),
    path('starterpage/',views.starter_page, name = 'starter_page'),
    path('terms/',views.terms, name = 'terms_page')
    
]