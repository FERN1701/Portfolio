from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import *
from . models import *
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator
from django.contrib import messages
from django.utils.crypto import get_random_string
from functools import wraps
from django.core.mail import send_mail
from django.utils import timezone
from pytz import timezone as tz
from django.conf import settings
from datetime import datetime, timedelta
from django.db.models import Sum, Max

@login_required(login_url='personal')
def home_admin(request):
    current_date = datetime.now()

    # Extract month, day, and year from the current date
    current_month = current_date.strftime('%b')  # Abbreviated month name
    current_day = current_date.strftime('%d')
    current_year = current_date.strftime('%Y')
    current_date = datetime.now()

# Subtract one month from the current date
    if current_date.month == 1:
        previous_month_date = datetime(current_date.year - 1, 12, current_date.day)
    else:
        previous_month_date = datetime(current_date.year, current_date.month - 1, current_date.day)

    # Get the name of the previous month and year
    previous_month_name = previous_month_date.strftime('%b')
    previous_year = current_date - timedelta(days=365)
    previous_year_name = previous_year.strftime('%Y')
        

    visitor_count = CountUser.objects.filter(countUserMonth=current_month, countUserDay=current_day, countUserYear=current_year).first()
# If there's no entry for the current date
    if not visitor_count:
        cppp = 0  # Initialize count to 0
        by_order = current_date.month  # Using the month number as order_month
        CountUser.objects.create(countUserCount=cppp, countUserMonth=current_month, countUserDay=current_day, countUserYear=current_year, order_month=by_order)


    current_date = datetime.now()
    month = current_date.strftime('%B')
    current_month = current_date.strftime('%b')  # Abbreviated month name
    current_day = current_date.strftime('%d')
    current_year = current_date.strftime('%Y')


    count_today = CountUser.objects.get(countUserMonth=current_month, countUserDay=current_day,countUserYear=current_year).countUserCount
    Max_user_in_a_month = CountUser.objects.filter(countUserMonth=current_month,countUserYear=current_year).aggregate(Max_user_in_a_month=Max('countUserCount'))['Max_user_in_a_month']
    if Max_user_in_a_month == 0:
        percentage_per_day = ( count_today / count_today ) * 100
    else:
        if count_today <= Max_user_in_a_month:
            percentage_per_day = ( count_today / Max_user_in_a_month) * 100
        else:
            percentage_per_day = ( Max_user_in_a_month / count_today) * 100


    count_month = CountUser.objects.filter(countUserMonth=current_month,countUserYear=current_year).aggregate(count_month=Sum('countUserCount'))['count_month']
    count_past_month = CountUser.objects.filter(countUserMonth=previous_month_name,countUserYear=current_year).aggregate(count_past_month=Sum('countUserCount'))['count_past_month']
    if count_past_month is None:
        percentage_month = 0
    else:
        if count_month <= count_past_month:
            percentage_month = ( count_month / count_past_month) * 100
        else:
            percentage_month = ( count_past_month / count_month) * 100

   

    visitcount = CountUser.objects.all().aggregate(Sum('countUserCount'))
    total_visitors = visitcount['countUserCount__sum']

    total_year = CountUser.objects.filter(countUserYear=current_year).aggregate(total_year=Sum('countUserCount'))['total_year']
    past_year = CountUser.objects.filter(countUserYear=previous_year_name).aggregate(past_year=Sum('countUserCount'))['past_year']
    if past_year is None:
        vistorsyearlypercent = 0
    else:
        if total_year <= past_year:
            vistorsyearlypercent = ( total_year / past_year) * 100
        else:
            vistorsyearlypercent = ( past_year / total_year) * 100

    monthly_counts = CountUser.objects.filter(countUserYear=current_year).values('countUserMonth').annotate(monthly_sum=Sum('countUserCount')).order_by('order_month')
    daily_counts = CountUser.objects.filter(countUserYear=current_year, countUserMonth=current_month).values('countUserDay').annotate(daily_sum=Sum('countUserCount')).order_by('countUserDay')

    messagez = contact_message.objects.filter(status="unread")[:8]
    detail_instance = get_object_or_404(details, pk=1)

    context = {
        'messagez':messagez,
        'detail_instance':detail_instance,
        'count_today':count_today,
        'count_month':count_month,
        'total_year':total_year,
        'vistorsyearlypercent':vistorsyearlypercent,
        'total_visitors':total_visitors,
        'current_year':current_year,
        'month':month,
        'monthly_counts':monthly_counts,
        'daily_counts':daily_counts,
        'current_day':current_day,
        'percentage_per_day':percentage_per_day,
        'percentage_month':percentage_month,
        'past_year':past_year,
        


    }
    return render(request, 'admin/index.html',context)


@login_required(login_url='personal')
def detaila(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = detail_form(request.POST, request.FILES, instance=detail_instance )
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('detaila')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = detail_form(instance=detail_instance)
    context = {
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
        
       
    }
    return render(request, 'admin/details.html',context)


@login_required(login_url='personal')
def visibi(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    control_panel = get_object_or_404(visibilities, pk=1)
    detail_instance = get_object_or_404(details, pk=1)
    context = {
        'detail_instance':detail_instance,
        'control_panel':control_panel,
        'messagez':messagez,
    }
    return render(request, 'admin/visibility.html',context)


@login_required(login_url='personal')
def toggle_for_youtube(request):
    control_panel = get_object_or_404(visibilities, pk=1)
    if control_panel.for_youtube == 0:
        control_panel.for_youtube = 1
        messages.success(request, "Hide")
    else:
        control_panel.for_youtube = 0
        messages.success(request, "Visible")
    control_panel.save()
    return redirect('visibi')


@login_required(login_url='personal')
def toggle_for_profile(request):
    
    control_panel = get_object_or_404(visibilities, pk=1)
    if control_panel.for_portfolio_profile == 0:
        control_panel.for_portfolio_profile = 1
        messages.success(request, "Hide")
    else:
        control_panel.for_portfolio_profile = 0
        messages.success(request, "Visible")
    control_panel.save()
    return redirect('visibi')


@login_required(login_url='personal')
def toggle_for_images(request):
    control_panel = get_object_or_404(visibilities, pk=1)
    if control_panel.for_two_detail_image == 0:
        control_panel.for_two_detail_image = 1
        messages.success(request, "Hide")
    else:
        control_panel.for_two_detail_image = 0
        messages.success(request, "Visible")
    control_panel.save()
    return redirect('visibi')


@login_required(login_url='personal')
def workdandcolab(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    colab = collaborations.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = collaborations_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('workdandcolab')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = collaborations_form()
    context = {
        'colab':colab,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/workdandcolab.html',context)


@login_required(login_url='personal')
def workdandcolab_edit(request,pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    colab_detail = get_object_or_404(collaborations, pk=pk)
    colab = collaborations.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = collaborations_form(request.POST, request.FILES, instance=colab_detail)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('workdandcolab')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = collaborations_form(instance=colab_detail)
    context = {
        'colab':colab,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/workdandcolab.html',context)

@login_required(login_url='personal')
def workdandcolab_delete(request,pk):
    delete_object = get_object_or_404(collaborations, pk=pk)
    delete_object.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('workdandcolab')


@login_required(login_url='personal')
def tech(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    tech = technolo.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = technolo_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('tech')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = technolo_form()
    context = {
        'tech':tech,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/technologies.html',context)


@login_required(login_url='personal')
def tech_delete(request,pk):
    delete_object = get_object_or_404(technolo, pk=pk)
    delete_object.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('tech')


@login_required(login_url='personal')
def tags(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    tagsz = prof_tags.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = tags_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('tags')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = tags_form()
    context = {
        'tagsz':tagsz,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/tags.html',context)

@login_required(login_url='personal')
def tag_delete(request,pk):
    delete_object = get_object_or_404(prof_tags, pk=pk)
    delete_object.delete()
    messages.success(request, "Deleted Successfully")
    return redirect('tags')


@login_required(login_url='personal')
def expiriences(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    expe = expirience.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = expirience_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('expiriences')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = expirience_form()
    context = {
        'expe':expe,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/expiriences.html',context)


@login_required(login_url='personal')
def expiriences_edit(request, pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    detail_expirience = get_object_or_404(expirience, pk=pk)
    expe = expirience.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = expirience_form(request.POST, request.FILES,instance=detail_expirience)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('expiriences')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = expirience_form(instance=detail_expirience)
    context = {
        'expe':expe,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/expiriences.html',context)

@login_required(login_url='personal')
def expiriences_delete(request, pk):
    detail_expirience = get_object_or_404(expirience, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('expiriences')



@login_required(login_url='personal')
def educations(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    edu = education.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = education_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('educations')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = education_form()
    context = {
        'edu':edu,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/education.html',context)


@login_required(login_url='personal')
def education_edit(request, pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    detail_education = get_object_or_404(education, pk=pk)
    edu = education.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = education_form(request.POST, request.FILES,instance=detail_education)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('educations')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = education_form(instance=detail_education)
    context = {
        'edu':edu,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/education.html',context)


@login_required(login_url='personal')
def education_delete(request, pk):
    detail_expirience = get_object_or_404(education, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('educations')

@login_required(login_url='personal')
def serves(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    ser = servicess.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = servicess_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('serves')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = servicess_form()
    context = {
        'ser':ser,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/services.html',context)


@login_required(login_url='personal')
def serves_edit(request, pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    detail_service = get_object_or_404(servicess, pk=pk)
    ser = servicess.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    if request.method == 'POST':
        form = servicess_form(request.POST, request.FILES, instance=detail_service)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('serves')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = servicess_form(instance=detail_service)
    context = {
        'ser':ser,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/services.html',context)

@login_required(login_url='personal')
def serves_delete(request, pk):
    detail_expirience = get_object_or_404(servicess, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('serves')



@login_required(login_url='personal')
def projectz(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    pro = projects.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = project_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('projectz')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = project_form()
    context = {
        'pro':pro,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/projects.html',context)


@login_required(login_url='personal')
def projectz_edit(request,pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    pro = projects.objects.all()
    pro_instance = get_object_or_404(projects, pk=pk)
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = project_form(request.POST, request.FILES, instance=pro_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('projectz')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = project_form(instance=pro_instance)
    context = {
        'pro':pro,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/projects.html',context)


@login_required(login_url='personal')
def projectz_delete(request, pk):
    detail_expirience = get_object_or_404(projects, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('projectz')



@login_required(login_url='personal')
def external(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    exte = extenal_contacts.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = extenal_contacts_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('external')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = extenal_contacts_form()
    context = {
        'exte':exte,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/external.html',context)

@login_required(login_url='personal')
def external_edit(request, pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    external_instrance = get_object_or_404(extenal_contacts, pk=pk)
    exte = extenal_contacts.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = extenal_contacts_form(request.POST, request.FILES, instance= external_instrance)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('external')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = extenal_contacts_form(instance= external_instrance)
    context = {
        'exte':exte,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/external.html',context)


@login_required(login_url='personal')
def external_delete(request, pk):
    detail_expirience = get_object_or_404(extenal_contacts, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('external')



@login_required(login_url='personal')
def social_medias(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    soc = social_media.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = social_media_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('social_medias')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = social_media_form()
    context = {
        'soc':soc,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/social_medias.html',context)


@login_required(login_url='personal')
def social_medias_edit(request,pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    soc_instance = get_object_or_404(social_media, pk=pk)
    soc = social_media.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = social_media_form(request.POST, request.FILES, instance=soc_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('social_medias')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = social_media_form( instance=soc_instance)
    context = {
        'soc':soc,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/social_medias.html',context)


@login_required(login_url='personal')
def social_medias_delete(request, pk):
    detail_expirience = get_object_or_404(social_media, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('social_medias')



@login_required(login_url='personal')
def Gallery_pannel(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    gal = galleries.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = galleries_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('Gallery_pannel')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = galleries_form()
    context = {
        'gal':gal,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/Gallery_pannel.html',context)

@login_required(login_url='personal')
def Gallery_pannel_edit(request,pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    galleries_instance = get_object_or_404(galleries, pk=pk)
    gal = galleries.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    
    if request.method == 'POST':
        form = galleries_form(request.POST, request.FILES, instance=galleries_instance)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Successfully")
            return redirect('Gallery_pannel')
        else:
             messages.error(request, "Please Try Again")
    else:
        form = galleries_form(instance=galleries_instance)
    context = {
        'gal':gal,
        'form':form,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/Gallery_pannel.html',context)

@login_required(login_url='personal')
def Gallery_pannel_delete(request, pk):
    detail_expirience = get_object_or_404(galleries, pk=pk)
    detail_expirience.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('Gallery_pannel')

@login_required(login_url='personal')
def Gallery(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    gal = galleries.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    context = {
        'gal':gal,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request, 'admin/gallery.html',context)


@login_required(login_url='personal')
def contact_us(request):
    messagez = contact_message.objects.filter(status="unread")[:8]
    contact = contact_message.objects.all()
    detail_instance = get_object_or_404(details, pk=1)
    context = {
        'contact':contact,
        'detail_instance':detail_instance,
        'messagez':messagez,
       
    }
    return render(request,'admin/contact_us.html',context)

@login_required(login_url='personal')
def contact_us_view(request, pk):
    messagez = contact_message.objects.filter(status="unread")[:8]
    contact_instance = get_object_or_404(contact_message, pk=pk)
    
    if contact_instance.status == "unread":
        contact_instance.status = "viewed"
        contact_instance.save()
        return redirect('contact_us_view', pk=pk)

    detail_instance = get_object_or_404(details, pk=1)
    context = {
        'contact_instance':contact_instance,
        'detail_instance': detail_instance,
        'messagez':messagez,
    }
    
    return render(request, 'admin/contact_us_view.html', context)


@login_required(login_url='personal')
def contact_us_delete(request, pk):
    del_contact = get_object_or_404(contact_message, pk=pk)
    del_contact.delete()
    messages.success(request, "Deleted Succesfully")
    return redirect('contact_us')
