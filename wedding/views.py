from django.conf import settings
from django.shortcuts import render
from guests.save_the_date import SAVE_THE_DATE_CONTEXT_MAP
from django.conf import settings
from django.core.mail import EmailMessage

def home(request):
    # email = EmailMessage('Testing', 'Testing email deployment from site', to=['Ensimmons623@gmail.com'])
    # email.send()
    return render(request, './home.html', context={
        'save_the_dates': SAVE_THE_DATE_CONTEXT_MAP,
        'support_email': settings.DEFAULT_WEDDING_REPLY_EMAIL,
        'website_url': settings.WEDDING_WEBSITE_URL,
        'couple_name': settings.BRIDE_AND_GROOM,
        'wedding_location': settings.WEDDING_LOCATION,
        'wedding_date': settings.WEDDING_DATE,
        'google_key': settings.GOOGLE_API_KEY
    })
