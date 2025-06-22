from django.shortcuts import render, redirect
from .models import ClassBooking
from django.http import HttpResponse

# Create your views here.

def view_home(request):
    return render(request,'index.html')

from django.shortcuts import render, redirect
from .models import ClassBooking
from django.http import HttpResponse

# View for booking a free class
def free_class_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        class_type = request.POST.get('class_type')

        # Saving the booking data to the database
        ClassBooking.objects.create(
            name=name, 
            email=email, 
            phone=phone, 
            class_type=class_type
        )

        # Redirect or response after successful booking
        return HttpResponse("Your free class has been booked successfully!")

    return render(request, 'free_class_form.html')

# View for booking a one-to-one class
def one_to_one_class_form_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        preferred_subject = request.POST.get('subject')

        # Saving the booking data to the database
        ClassBooking.objects.create(
            name=name, 
            email=email, 
            phone=phone, 
            class_type='One-to-One',
            preferred_subject=preferred_subject
        )

        # Redirect or response after successful booking
        return HttpResponse("Your one-to-one class has been booked successfully!")

    return render(request, 'one_to_one_class_form.html')
