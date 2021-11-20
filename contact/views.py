from django.shortcuts import render
from .forms import *


# Create your views here.

def contact_us(request):
    form = ContactForm(request.POST or None)
    context = {
        'forms': form,
    }
    if form.is_valid():
        name = form.cleaned_data.get('name')
        email = form.cleaned_data.get('email')
        title = form.cleaned_data.get('title')
        message = form.cleaned_data.get('message')
        print(name + '  ' + email + '  ' + title + '  ' + message) 
    return render(request, 'contact_us.html', context)
