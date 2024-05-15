
from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing

urlpatterns = [
    path('',views.home,name = 'home'),
    path('project/',views.project,name = 'project'),
    path('gallery/',views.gallery,name = 'gallery'),
    path('tyrannosaur/',views.tyrannosaur,name = 'tyrannosaur'),  
    path('personal/',views.personal,name = 'personal'), 
    path('logout/',views.logoutUser,name = 'logoutUser'),
    #path('about/', views.about_view, name='about'),
    #path('features/', views.feature_view, name='features'),
    #path('developers/', views.Developers, name='developers'),
    #path('contact/', views.ContactUS, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
