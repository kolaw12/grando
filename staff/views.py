from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import login,logout,authenticate
from carapp.models import *
from django.contrib import messages
# Create your views here.
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
def sign_up(request):
    if request.method == 'POST':
        reg = RegistrationForm(request.POST)
        if reg.is_valid:
            try:
                reg.save()
                messages.success(request, 'Registration Successful')
                return redirect('staff:signin_page')
            except:
                print('Form errors:',reg.errors)
                for field,errors in reg.errors.items():
                    for error in errors:
                        messages.error(request, f"{field}:{error}")
    else:
        reg = RegistrationForm()
    return render(request, './staff/sign-up.html',{'reg':reg} )
def sign_in(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('staff:dashboard_page')
        else:
            messages.error(request,"username or password does not exist")
    return render(request, './staff/sign-in.html')
def dashboard(request):
    bookings = Booking.objects.all()
    context = {
        "bookings": bookings
    }
    return render(request, './staff/dashboard.html', context)
def user_dashboard(request):
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
    return render(request, './staff/user-dashboard.html',{ 'form' : bookings })
def product_dashboard(request):
    rooms = Room.objects.all()
    context ={
        'rooms': rooms
    }
    return render(request, './staff/product-dashboard.html', context)

def edit_booking(request, bookin_id):
    single_request =Booking.objects.get(id = bookin_id)
    if request.method == 'POST':
        bookings= BookingForm(request.POST , instance= single_request)
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
        bookings = BookingForm(instance=single_request)

    return render(request, './staff/edit-booking.html', {"form":bookings})
def delete_booking(request, bookin_id):
    single_request = Booking.objects.get(id = bookin_id)
    single_request.delete()
    return redirect('staff:dashboard_page')

def logout_user(request):
    logout(request)
    return redirect('staff:signin_page')