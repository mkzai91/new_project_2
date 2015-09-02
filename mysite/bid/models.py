from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from mysite import settings
from tinymce.widgets import TinyMCE
from tinymce import models as tinymce_models
from datetime import date, timedelta
from filebrowser.fields import FileBrowseField

imageextensions= ['.jpg', '.jpeg', '.gif','.png', '.tif','.tiff']

class Product(models.Model):
    name = models.CharField(max_length=30)
    publish_date=models.DateField(auto_now=False,auto_now_add=True)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    expire_date=models.DateField(auto_now=False,auto_now_add=False, default=date.today()+timedelta(7))
    bid_price=models.DecimalField(max_digits=8,decimal_places=2, default=0)
    photo = models.ImageField(upload_to='') 
    website=models.CharField(max_length=500)
    description= tinymce_models.HTMLField()
    total_view= models.IntegerField(default=0)
    today_view= models.IntegerField(default=0)
    buyer=models.CharField(max_length=150, default=None, null=True,blank=True)
    
    
class WorkSheet(models.Model):
    title = models.CharField(max_length= 150, default ='')
    creator = models.ForeignKey(User, default=None, blank=True, null=True)
    file = models.ImageField(upload_to='')
    pub_date=models.DateTimeField(auto_now=True,auto_now_add=True)
    pdf= models.FileField(upload_to='')
    image = FileBrowseField("Image", max_length=200, directory="", extensions=imageextensions, blank=True, null=True, default='')

class Member(models.Model):
    username = models.CharField(max_length= 150, default ='')
    password = models.CharField(max_length= 15, default ='')
    name = models.CharField(max_length= 150, default ='')
    email = models.CharField(max_length= 150, default ='')
    cart_size = models.IntegerField(default=0)