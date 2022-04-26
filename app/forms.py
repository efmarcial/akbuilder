import imp
from .models import *
from django import forms
from django.forms import fields, widgets


class ContactForm(forms.ModelForm):
    #Specify the models that is being used 
    
    class Meta:

        model = Contact

        fields = ['fullname', 'message', 'email', 'phone_number']

        widgets = {
            'fullname' : widgets.TextInput(attrs={
                'class' : 'input', 
                'placeholder' : 'Full name...', 
                'type' : 'text',
                'name' : 'name',
                'required' : ''
            }),

            'email' : widgets.EmailInput(attrs={
                'class' : 'input', 
                'placeholder' : 'Email...',
                'type' : 'email',
                'name' : 'email',
                'required' : ''
            }),

            'phone_number' : widgets.TextInput(attrs={
                'class' : 'input',
                'id' : 'myNumber',
                'placeholder' : 'Phone Number...',
                'type' : 'tel',
                'name' : 'phone_number',
                'datamask' : '999-999-9999',
                'pattern' : "[0-9]{3}-[0-9]{3}-[0-9]{4}",
                'required' : ''
            }),

            'message' : widgets.Textarea(attrs={
                'name' : 'message', 
                'placeholder' : 'How can we help you today?',
                'class' : 'textarea',
                'required' : '',
            })
        }


