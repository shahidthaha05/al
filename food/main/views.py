from django.shortcuts import render

# Create your views here.


from django.shortcuts import render


def home(request):
    return render(request, 'user.html/home.html')

def about(request):
    return render(request, 'user.html/about.html')

def menu(request):
    return render(request, 'user.html/menu.html')

def gallery(request):
    return render(request, 'user.html/gallery.html')





# views.py

from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = 'New Contact Form Submission'
            body = (
                f"Name: {form.cleaned_data['name']}\n"
                f"Email: {form.cleaned_data['email']}\n\n"
                f"Message:\n{form.cleaned_data['message']}"
            )
            send_mail(subject, body, form.cleaned_data['email'], ['shahidthaha4@gmail.com'])
            messages.success(request, 'Thanks! Your message has been sent.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'user.html/contact.html', {'form': form})
