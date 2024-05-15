from django.db import models

# Create your models here.
class details(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    portfolio_profile = models.FileField(upload_to="Portfolio Profile", max_length=100, null=True)
    Details_photo1 = models.FileField(upload_to="Details Photos", max_length=100, null=True)
    Details_photo2 = models.FileField(upload_to="Details Photos", max_length=100, null=True)
    years = models.IntegerField()
    based_expirience = models.CharField(max_length=288)
    description = models.TextField()
    youtube = models.CharField(max_length=1888, null=True)
    messenger = models.CharField(max_length=1888, null=True)
    googlemap = models.CharField(max_length=1888, null=True)
    cvfile = models.FileField(upload_to="Curriculum vitae", max_length=100)


class visibilities(models.Model):
    for_youtube  = models.IntegerField(default="0")
    for_portfolio_profile  = models.IntegerField(default="0")
    for_two_detail_image  = models.IntegerField(default="0")

class collaborations(models.Model):
    title = models.CharField(max_length=188)
    total = models.IntegerField()
    description = models.TextField()

class technolo(models.Model):
    tech_icon = models.CharField( max_length=188)

class prof_tags(models.Model):
    tagname = models.CharField( max_length=188)

class expirience(models.Model):
    role = models.CharField(max_length=88)
    date1 = models.CharField(max_length=88)
    date2 = models.CharField(max_length=88)
    location = models.CharField( max_length=188)

class education(models.Model):
    course = models.CharField(max_length=88)
    date1 = models.CharField(max_length=88)
    date2 = models.CharField(max_length=88)
    location = models.CharField( max_length=188)

class servicess(models.Model):
    service = models.CharField( max_length=188)
    description = models.CharField(max_length=388)

class projects(models.Model):
    cho = (
        ('hide1', 'Hide to portfolio'),
        ('hide2', 'Hide to Index'),
        ('open', 'Visible to All'),
    )
    project_banner = models.FileField(upload_to="Projects", max_length=188)
    title = models.CharField( max_length=88)
    link = models.CharField( max_length=288)
    description = models.TextField()
    highlight = models.CharField(default='open', choices=cho, max_length=28)


class extenal_contacts(models.Model):
    type_detail = (
        ('email','Email'),
        ('number','Phone Number'),
        ('normal','Normal'),
    )
    title = models.CharField( max_length=50)
    content = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices = type_detail)

class social_media(models.Model):
    ICON_CHOICES = (
    ('fa-facebook','facebooks'),
    ('fa-gitlab','Git Lab'),
    ('fa-github','Git Hub'),
    ('fa-messenger','Messenger'),
    ('fa-twitter','Twitter'),
    ('fa-google','Google'),
    ('fa-linkedin','LinkedIn'),
    ('fa-youtube','Youtube'),
    ('fa-instagram','Instagram'),
    ('fa-pinterest','Pinterest'),
    ('fa-snapchat-ghost','Snapchat Ghost'),
    ('fa-skype','Skype'),
    ('fa-android','Andriod'),
    ('fa-dribbble','Dribble'),
    ('fa-vimeo','Vimeo'),
    ('fa-tumblr','Tumblr'),
    ('fa-vine','Vine'),
    ('fa-foursquare','Foursquare'),
    ('fa-stumbleupon','Stumbleupon'),
    ('fa-flickr','Flickr'),
    ('fa-yahoo','Yahoo'),
    ('fa-soundcloud','Soundcloud'),
    ('fa-reddit','Reddit'),
    ('fa-rss','Rss'),

)
    icon = models.CharField(choices=ICON_CHOICES, max_length=50)
    link = models.CharField(max_length=188)

class galleries(models.Model):
    gal_stat = (
        ('hide','Hide'),
        ('visible','Visible'),
    )
    title = models.CharField( max_length=88)
    photo = models.FileField(upload_to="Gallery", max_length=188)
    description = models.TextField()
    status = models.CharField(max_length=50,choices=gal_stat)


class contact_message(models.Model):
    contact_status = (
        ('viewed','viewed'),
        ('unread','Unread'),
    )
    name = models.CharField(max_length=188)
    email = models.CharField(max_length=188)
    subject = models.CharField(max_length=188)
    message = models.TextField()
    date_sent = models.DateTimeField( auto_now=True, auto_now_add=False)
    status = models.CharField(max_length=50, default="unread" ,choices= contact_status)


class CountUser(models.Model):
    countUserCount = models.IntegerField(default=0)
    countUserMonth = models.CharField(max_length=3)  # Assuming abbreviated month names like 'Jan', 'Feb', etc.
    countUserDay = models.CharField(max_length=2)
    countUserYear = models.CharField(max_length=4)
    order_month = models.IntegerField()