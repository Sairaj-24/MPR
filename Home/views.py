from django.shortcuts import render

# Create your views here.

def view_home(request):
    return render(request,'index.html')

def free_class_form_view(request):
    return render(request, 'free_class_form.html')

def one_to_one_class_form_view(request):
    return render(request, 'one_to_one_class_form.html')