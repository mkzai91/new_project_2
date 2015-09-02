from django.conf.urls import url
from django.conf import settings
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.mainview, name='name'),
    # ex: /polls/5/
    url(r'^addproduct', views.addproduct, name='addproduct'),
    url(r'^upload',views.upload,name='upload'),
    url(r'^showimage',views.showimage,name='showimage'),
    url(r'^description',views.description,name='description'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^payment', views.payment, name='payment'),
    url(r'^cart', views.cart, name='cart'),
]
