from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from Admin.models import *
from .forms import *
from django.utils.crypto import get_random_string
from functools import wraps
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db.models import Q
from Admin.forms import *
from datetime import datetime, timedelta
from django.template.loader import render_to_string
from django.utils.html import strip_tags



def home(request):
    
    client_ip_address = request.META.get('REMOTE_ADDR', '')

    # Retrieve the stored IP addresses from session
    stored_ip_address_1 = request.session.get('stored_ip_address_1')
    stored_ip_address_2 = request.session.get('stored_ip_address_2')

    if not stored_ip_address_1 or not stored_ip_address_2:
        # If either of the stored IP addresses is not present in the session, store the current IP address
        request.session['stored_ip_address_1'] = client_ip_address
        request.session['stored_ip_address_2'] = client_ip_address


    if stored_ip_address_1 != client_ip_address or stored_ip_address_2 != client_ip_address:
        # If the current IP address is different from either of the stored IP addresses, update both
        request.session['stored_ip_address_1'] = client_ip_address
        request.session['stored_ip_address_2'] = client_ip_address
     

    # If the IP address is the same in both stored variables

    soc = social_media.objects.all()
    exte = extenal_contacts.objects.all()
    pro = projects.objects.exclude(Q(highlight="hide2") | Q(highlight="hide1"))
    ser = servicess.objects.all()
    edu = education.objects.all()
    expe = expirience.objects.all()
    prf = prof_tags.objects.all()
    colab = collaborations.objects.all()
    tech = technolo.objects.all()
    control_panel = get_object_or_404(visibilities, pk=1)
    detail_instance = get_object_or_404(details, pk=1)
    
    #:::::::::::::::::::
    current_date = datetime.now()

    # Extract month, day, and year from the current date
    current_month = current_date.strftime('%b')  # Abbreviated month name
    current_day = current_date.strftime('%d')
    current_year = current_date.strftime('%Y')

    # Query the database to check if there's an entry for the current date
    visitor_count = CountUser.objects.filter(countUserMonth=current_month, countUserDay=current_day, countUserYear=current_year).first()

    if visitor_count:
        if stored_ip_address_1 != client_ip_address:
            cpp = visitor_count.countUserCount
            cppp = cpp + 1
            visitor_count.countUserCount = cppp
            visitor_count.save()

        # If there's no entry for the current date
    else:
            cppp = 1
            by_order = current_date.month  # Using the month number as order_month
            CountUser.objects.create(countUserCount=1, countUserMonth=current_month, countUserDay=current_day, countUserYear=current_year, order_month=by_order)
    #:::::::::::::::::::

    if request.method == 'POST':
        contact_form = contact_message_form(request.POST, request.FILES)
        if contact_form.is_valid():
            subject = 'You have a new message inquiry from the portfolio from ' + contact_form.cleaned_data['name']
            message = 'Message : ' + contact_form.cleaned_data['message']
            from_email = "argonfernando453@gmail.com"
            to_email = "argonfernando453@gmail.com"
            send_mail(subject, message, from_email, [to_email], fail_silently=False)


            subject = f"Hi, This is {detail_instance.firstname} {detail_instance.lastname}"
            html_message = render_to_string('email_template.html', {
                'firstname': detail_instance.firstname,
                'lastname': detail_instance.lastname,
                'messenger': detail_instance.messenger,
            })
            plain_message = strip_tags(html_message)  # Fallback for plain text email clients
            from_email = "argonfernando453@gmail.com"
            to_email = contact_form.cleaned_data['email']
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message, fail_silently=False)

           

            contact_form.save()
            messages.success(request, "Message sent successfully")
            return redirect('home')
        else:
            messages.error(request, "Please Try Again")
    else:
        contact_form = contact_message_form()


    context = {
        'contact_form':contact_form,
        'soc':soc,
        'exte':exte,
        'pro':pro,
        'ser':ser,
        'edu':edu,
        'expe':expe,
        'prf':prf,
        'tech':tech,
        'control_panel':control_panel,
        'colab':colab,
       'detail_instance':detail_instance,
       'current_day':current_day
    }
    return render(request,'index.html',context)

def project(request):
    soc = social_media.objects.all()
    exte = extenal_contacts.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    pro = projects.objects.exclude(Q(highlight="hide1"))

    if request.method == 'POST':
        contact_form = contact_message_form(request.POST, request.FILES)
        if contact_form.is_valid():
            subject = 'You have a new message inquiry from the portfolio from ' + contact_form.cleaned_data['name']
            message = 'Message : ' + contact_form.cleaned_data['message']
            from_email = "argonfernando453@gmail.com"
            to_email = "argonfernando453@gmail.com"
            send_mail(subject, message, from_email, [to_email], fail_silently=False)

            
            subject = f"Hi, This is {detail_instance.firstname} {detail_instance.lastname}"
            html_message = render_to_string('email_template.html', {
                'firstname': detail_instance.firstname,
                'lastname': detail_instance.lastname,
                'messenger': detail_instance.messenger,
            })
            plain_message = strip_tags(html_message)  # Fallback for plain text email clients
            from_email = "argonfernando453@gmail.com"
            to_email = contact_form.cleaned_data['email']
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message, fail_silently=False)

            contact_form.save()
            messages.success(request, "Message sent successfully")
            return redirect('project')
        else:
            messages.error(request, "Please Try Again")
    else:
        contact_form = contact_message_form()
    context = {
       'contact_form':contact_form,
       'soc':soc,
       'pro':pro,
       'exte':exte,
       'detail_instance':detail_instance,
    }
    return render(request,'project.html',context)


def gallery(request):
    gal = galleries.objects.exclude(status="hide")
    soc = social_media.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    exte = extenal_contacts.objects.all()

    if request.method == 'POST':
        contact_form = contact_message_form(request.POST, request.FILES)
        if contact_form.is_valid():
            subject = 'You have a new message inquiry from the portfolio from ' + contact_form.cleaned_data['name']
            message = 'Message : ' + contact_form.cleaned_data['message']
            from_email = "argonfernando453@gmail.com"
            to_email = "argonfernando453@gmail.com"
            send_mail(subject, message, from_email, [to_email], fail_silently=False)
            
            subject = f"Hi, This is {detail_instance.firstname} {detail_instance.lastname}"
            html_message = render_to_string('email_template.html', {
                'firstname': detail_instance.firstname,
                'lastname': detail_instance.lastname,
                'messenger': detail_instance.messenger,
            })
            plain_message = strip_tags(html_message)  # Fallback for plain text email clients
            from_email = "argonfernando453@gmail.com"
            to_email = contact_form.cleaned_data['email']
            send_mail(subject, plain_message, from_email, [to_email], html_message=html_message, fail_silently=False)
            contact_form.save()
            messages.success(request, "Message sent successfully")
            return redirect('gallery')
        else:
            messages.error(request, "Please Try Again")
    else:
        contact_form = contact_message_form()
    context = {
        'contact_form':contact_form,
        'soc':soc,
        'gal':gal,
        'exte':exte,
        'detail_instance':detail_instance,
       
    }
    return render(request,'gallery.html',context)

#::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def tyrannosaur(request):
    form = MyUserCreationForm()
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = int(get_random_string(length=6, allowed_chars='1234567890'))
            user.code = int(get_random_string(length=6, allowed_chars='1234567890'))
            user.save()
            messages.success(request, 'Account Created Successfully')
            return redirect('personal')
        else:
            messages.error(request, 'An error occurred during registration')
    context = {
        'form':form
       
       
    }
    return render(request, 'signup.html', context)




def personal(request):
    page = 'login'
    detail_instance = get_object_or_404(details, pk=1)
    if request.user.is_authenticated:
        return redirect('home_admin')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'User does not exist')
            return render(request, 'signin.html', {'page': page, 'detail_instance':detail_instance,})

        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Check user's status and code
            user.log_status = "online"
            user.save()
            login(request, user)
            messages.success(request,'Login succesfully')
            return redirect('home_admin')
        else:
            messages.error(request, 'Wrong Admin Credentials')
    context = {
        
       'page': page,
       'detail_instance':detail_instance,
    }
    return render(request, 'signin.html', context)

def logoutUser(request):
    user = request.user
    user.log_status = "offline"
    user.save()
    logout(request)
    return redirect('home')

def custom_404(request, exception):
    return render(request, '404.html', status=404)