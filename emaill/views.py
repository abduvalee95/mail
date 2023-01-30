from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse

def send_email(request):
    subject = 'Happy birthday email'
    subscribers = [
        {'first_name': 'John', 'last_name': 'Doe', 'birthday': '10/12/2022'},
        {'first_name': 'Jane', 'last_name': 'Doe', 'birthday': '11/12/2022'},
        {'first_name': 'Bob', 'last_name': 'Smith', 'birthday': '12/12/2022'},
    ]
    from_email = 'from@example.com'
    for subscriber in subscribers:
        message = render_to_string('email_template.html', {'subscriber': subscriber})
        recipient_list = [subscriber['email']]
        send_mail(subject, message, from_email, recipient_list, html_message=message)
    return HttpResponse('Emails sent')
