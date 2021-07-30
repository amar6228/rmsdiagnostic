from django.http.response import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from twilio.rest import Client
from django.conf import settings


# Create your views here.
def home(request):
    return render(request, 'homeapp/home.html')


def about(request):
    return render(request, 'homeapp/about.html')

def contact(request):

    name= request.POST.get('name')
    email = request.POST.get('email')
    phone= request.POST.get('phone')
    message = request.POST.get('message')

    print(name,email,phone,message)

    message_to_broadcast = ("Have you played the incredible TwilioQuest yet? Grab it here: https://www.twilio.com/quest")
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
    for recipient in settings.SMS_BROADCAST_TO_NUMBERS:
        if recipient:
            client.messages.create(to=recipient,
            from_=settings.TWILIO_NUMBER,
            body=message_to_broadcast)
        return HttpResponse("messages sent!", 200)

    if name and message and email and phone:
        
        send_mail('RMS one mail From: '+name+' , '+phone, message, email, ['malhotrakundan01@gmail.com'] )
        # except BadHeaderError:
        #     return HttpResponse('Invalid header found.')
        # return HttpResponseRedirect('/contact/')
    else:
        # In reality we'd use a form class
        # to get proper validation errors.
        # return HttpResponse('Make sure all fields are entered and valid.')

        return render(request, 'homeapp/contact.html')


def offers(request):
    return render(request, 'homeapp/offers.html')

def faq(request):
    return render(request, 'homeapp/faq.html')

def packages(request):
    return render(request, 'homeapp/packages.html')

# Test view here

def test(request): 
    return render(request, 'homeapp/test.html')
    
def test_package(request, title): 
    return render(request, 'homeapp/test_package.html', {'title':title} )

# Test views end here

def centers(request):
    return render(request, 'homeapp/centers.html')
    









