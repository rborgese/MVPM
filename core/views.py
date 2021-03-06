from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from .forms import ContactForm
from promanage.forms import RentalApplicationForm
from promanage.models import RentalProperty,RentalApplication

def index(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data.get("name")
        email = form.cleaned_data.get("email")
        subject = form.cleaned_data.get("subject")
        message = form.cleaned_data.get("message")
        message = "Name: " + name + "\n"+"Email: "+ email +"\n"+"Message: "+ message

        send_mail(
            subject,
            message,
            email,
            [settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

    context ={
            "form":form
        }
    return render(request, "core/index.html", context)

def home_for_rent(request):
    homes = RentalProperty.objects.filter(is_available=True)
    context = {
        'homes':homes,
        'user':request.user
    }
    return render(request,'core/homeforrent.html',context)

def home_detail(request,id = None):
    instance = get_object_or_404(RentalProperty,id = id)
    form = RentalApplicationForm(request.POST or None)
    if form.is_valid():
        form_instance = form.save(commit=False)
        form_instance.rent_property = instance
        form_instance.save()
        messages.success(request,"request sent successfully")
    context = {
        'user':request.user,
        'instance':instance,
        'form':form
    }
    return render(request,'core/homedetail.html',context)