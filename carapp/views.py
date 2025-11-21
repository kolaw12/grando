from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from .models import *
from django.contrib import messages
from .forms import BookingForm

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
# Create your views here.
def index(request):
    # rooms = Room.objects.all()[:3]
    rooms = []
    return render(request, 'home.html', {'rooms':rooms})
def about(request):
    rooms = Room.objects.all()[:2]
    return render(request, 'about.html', {'rooms':rooms})
def amenity(request):
    return render(request, 'amenities.html')
def booking(request):
    if request.method == 'POST':
        bookings = BookingForm(request.POST)
        if bookings.is_valid():
            bookings.save()
            name = bookings.cleaned_data['name']
            email = bookings.cleaned_data['email']
            arrival_date = bookings.cleaned_data['arrival_date']
            room = bookings.cleaned_data['room']
            mail_subject = 'BOOKING RECIEVED'
            mail_context ={
                'name':name,
                'email': email,
                'arrival_date': arrival_date,
                'room': room
            }
            html_message = render_to_string('booking-mail.html', mail_context)
            plain_text = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            try:
                email_message = EmailMessage(mail_subject,plain_text,from_email,to=recipient_list)
                email_message.send()
                messages.success(request, 'Bookings successfully')
            except(Exception) as e:
                messages.error(request, 'An error occured')
                
    else:
        bookings = BookingForm()
    return render(request, 'booking.html', {'bookings':bookings})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        subject = request.POST.get('subject')
        ContactForm.objects.create(name=name,email=email,message=message,subject=subject)
        messages.success(request, 'Message sent successfully')
    return render(request, 'contact.html')
def event(request):
    return render(request, 'events.html')
def gallery(request):
    return render(request, 'gallery.html')
def location(request):
    return render(request, 'location.html')
def offer(request):
    return render(request, 'offers.html')
def privacy(request):
    return render(request, 'privacy.html')
def restaurant(request):
    return render(request, 'restaurant.html')
def room_details(request, room_id):
    detail = get_object_or_404(Room, id = room_id)
    return render(request, 'room-details.html', {'detail': detail})
def rooms(request):
    rooms = Room.objects.all().order_by('-created')
    return render(request, 'rooms.html', {'rooms': rooms})
def starter_page(request):
    return render(request, 'starter-page.html')
def terms(request):
    return render(request, 'terms.html')