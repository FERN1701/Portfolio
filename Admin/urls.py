
from django.urls import path
from . import views

from django.conf import settings

from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.urls import path, include
#for Routing

urlpatterns = [
    path('',views.home_admin,name = 'home_admin'),
    path('details/',views.detaila,name = 'detaila'),
    path('works/',views.workdandcolab,name = 'workdandcolab'),
    path('works/<int:pk>/update/',views.workdandcolab_edit,name = 'workdandcolab_edit'),
    path('works/<int:pk>/delete/',views.workdandcolab_delete,name = 'workdandcolab_delete'),
    path('technologies/',views.tech,name = 'tech'),
    path('technologies/<int:pk>/delete/',views.tech_delete,name = 'tech_delete'),
    path('tags/',views.tags,name = 'tags'),
    path('tags/<int:pk>/delete/',views.tag_delete,name = 'tag_delete'),
    path('expiriences/',views.expiriences,name = 'expiriences'),
    path('expiriences/<int:pk>/update/',views.expiriences_edit,name = 'expiriences_edit'),
    path('expiriences/<int:pk>/delete/',views.expiriences_delete,name = 'expiriences_delete'),
    path('education/',views.educations,name = 'educations'),
    path('education/<int:pk>/update/',views.education_edit,name = 'education_edit'),
    path('education/<int:pk>/delete/',views.education_delete,name = 'education_delete'),
    path('services/',views.serves,name = 'serves'),
    path('services/<int:pk>/update/',views.serves_edit,name = 'serves_edit'),
    path('services/<int:pk>/delete/',views.serves_delete,name = 'serves_delete'),
    path('projects/',views.projectz,name = 'projectz'),
    path('projects/<int:pk>/update/',views.projectz_edit,name = 'projectz_edit'),
    path('projects/<int:pk>/delete/',views.projectz_delete,name = 'projectz_delete'),
    path('external/',views.external,name = 'external'),
    path('external/<int:pk>/update/',views.external_edit,name = 'external_edit'),
    path('external/<int:pk>/delete/',views.external_delete,name = 'external_delete'),
    path('social_medias/',views.social_medias,name = 'social_medias'),
    path('social_medias/<int:pk>/update/',views.social_medias_edit,name = 'social_medias_edit'),
    path('social_medias/<int:pk>/delete/',views.social_medias_delete,name = 'social_medias_delete'),
    path('Gallery/pannel/',views.Gallery_pannel,name = 'Gallery_pannel'),
    path('Gallery/pannel/<int:pk>/update/',views.Gallery_pannel_edit,name = 'Gallery_pannel_edit'),
    path('Gallery/pannel/<int:pk>/delete/',views.Gallery_pannel_delete,name = 'Gallery_pannel_delete'),
    path('Gallery/',views.Gallery,name = 'Gallery'),
    path('Contact/',views.contact_us,name = 'contact_us'),
    path('Contact/<int:pk>/view/',views.contact_us_view,name = 'contact_us_view'),
    path('Contact/<int:pk>/delete/',views.contact_us_delete,name = 'contact_us_delete'),
   

    path('visibility/',views.visibi,name = 'visibi'),
    path('toggle_for_youtube/',views.toggle_for_youtube,name = 'toggle_for_youtube'),
    path('toggle_for_profile/',views.toggle_for_profile,name = 'toggle_for_profile'),
    path('toggle_for_images/',views.toggle_for_images,name = 'toggle_for_images'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
