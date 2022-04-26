
from django.shortcuts import render
from django.http import BadHeaderError, HttpResponse
from django.core.mail import EmailMessage, send_mail
from django.contrib.messages import get_messages
from django.contrib import messages
from django.template.loader import render_to_string, get_template

# import images and contact form
from .models import *
from .forms import *

# Create your views here.

def index(request):

    # Get images for  the gallary
    try:
        images = GalleryImage.objects.all()
    except GalleryImage.DoesNotExist:
        images = None

    if request.method == "GET":

        contact_form = ContactForm()

    else: 

        contact_form = ContactForm(request.POST or None)

        if contact_form.is_valid():

            fullname = request.POST.get['name']
            email = request.POST.get['email']
            contact_message = request.POST.get['message']
            phone_number = request.POST.get['phone_number']

            subject = f"A&K Contact Page | {fullname}"

            # email context set up to be rendered to email html template
            email_context = {
                'fullname' : fullname, 
                'email' : email, 
                'message' : contact_message, 
                'phone_number' : phone_number
            }
            
            # Render the html file to be passed to the email message
            msg_html = render_to_string('app/email.html', context=email_context)

            # Check if the subject and message are valid before sending 
            if subject and contact_message:
                try:
                    
                    email = EmailMessage(
                        subject, 
                        msg_html, 
                        'from@emaple.com',
                        '[from@example.com]',
                    )

                    email.content_subtype = 'html'
                    email.send

                    # Send a message on send
                    messages.info(request, "Message sent!")

                    # After message send then reset the contact form by sending the empty form
                    second_form = ContactForm()

                    second_context = {
                        'images' : images,
                        'contact_form' : second_form
                    }

                    return render(request, 'app/index.html', second_context)
                    
                except BadHeaderError:
                    second_form = ContactForm()

                    second_context = {
                        'images' : images,
                        'contact_form' : second_form
                    }
                    return render(request, 'app/index.html', second_context)



    context = {
        'images' : images, 
        'contact_form' : contact_form
    }

    return render(request, 'app/index.html', context=context)
    
