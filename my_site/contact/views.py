from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.template.loader import render_to_string
# Create your views here.
def contact(request):
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']
            content=form.cleaned_data['content']

            html=render_to_string('contact/emails/contactform.html',{
                'name':name,
                'email':email,
                'content':content
            })
            print("the post is valid")
            send_mail('The contact form subject', 'This is the message','noreply@trokhin87.com',['trokhin87@gnail.com'],html_message=html)
            return redirect('blog-home')
    else:
        form=ContactForm()
    return render(request,
                  'contact/contact.html',
                  {
                  'form':form
                  }
                )
