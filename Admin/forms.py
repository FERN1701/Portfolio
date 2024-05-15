from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms

class detail_form(ModelForm):
    class Meta:
        model = details
        fields = ['firstname','lastname','portfolio_profile', 'Details_photo1','Details_photo2', 'years', 'based_expirience','description','youtube','messenger','googlemap','cvfile']
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'portfolio_profile':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'Details_photo1':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'Details_photo2':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'years':forms.NumberInput(attrs={'class':'form-control'}),
            'based_expirience':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','id': 'summernote'}),
            'youtube':forms.TextInput(attrs={'class':'form-control'}),
            'messenger':forms.TextInput(attrs={'class':'form-control'}),
            'googlemap':forms.TextInput(attrs={'class':'form-control'}),
            'cvfile':forms.ClearableFileInput(attrs={'class':'form-control'}),
              
        }
   
class collaborations_form(ModelForm):
    class Meta:
        model = collaborations
        fields = ['title','total','description']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
              
        }

class technolo_form(ModelForm):
    class Meta:
        model = technolo
        fields = ['tech_icon']
        widgets = {
            'tech_icon':forms.TextInput(attrs={'class':'form-control'}),
                  
        }

class tags_form(ModelForm):
    class Meta:
        model = prof_tags
        fields = ['tagname']
        widgets = {
            'tagname':forms.TextInput(attrs={'class':'form-control'}),
                  
        }
      
class expirience_form(ModelForm):
    class Meta:
        model = expirience
        fields = ['role','date1','date2','location']
        widgets = {
            'role':forms.TextInput(attrs={'class':'form-control'}),
            'date1':forms.TextInput(attrs={'class':'form-control'}),
            'date2':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
              
        }

class education_form(ModelForm):
    class Meta:
        model = education
        fields = ['course','date1','date2','location']
        widgets = {
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'date1':forms.TextInput(attrs={'class':'form-control'}),
            'date2':forms.TextInput(attrs={'class':'form-control'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
              
        }

     
class servicess_form(ModelForm):
    class Meta:
        model = servicess
        fields = ['service','description']
        widgets = {
            'service':forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control' ,'id': 'summernote'}),
        }

class project_form(ModelForm):
    class Meta:
        model = projects
        fields = ['project_banner','title','link','highlight','description']
        widgets = {
            'project_banner':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'link':forms.TextInput(attrs={'class':'form-control'}),
            'highlight':forms.Select(attrs={'class':'form-control'}),
            'description': forms.Textarea(attrs={'class':'form-control','id': 'summernote'}),
        }

class extenal_contacts_form(ModelForm):
    class Meta:
        model = extenal_contacts
        fields = ['title','content','type']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'content':forms.TextInput(attrs={'class':'form-control'}),
            'type':forms.Select(attrs={'class':'form-control'}),
        }  


class social_media_form(ModelForm):
    class Meta:
        model = social_media
        fields = ['icon','link']
        widgets = {
            
            'icon':forms.Select(attrs={'class':'form-control'}),
            'link':forms.TextInput(attrs={'class':'form-control'}),
        } 


class galleries_form(ModelForm):
    class Meta:
        model = galleries
        fields = ['title','photo','description','status']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'photo':forms.ClearableFileInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control','id': 'summernote'}),
            'status':forms.Select(attrs={'class':'form-control'}),
        } 
class contact_message_form(ModelForm):
    class Meta:
        model = contact_message
        fields = ['name','email','subject','message']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control', 'id':'name'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'email'}),
            'subject':forms.TextInput(attrs={'class':'form-control', 'id':'subject'}),
            'message':forms.Textarea(attrs={'class':'form-control','id': 'summernote', 'style':'height: 100px'}),
        } 


     