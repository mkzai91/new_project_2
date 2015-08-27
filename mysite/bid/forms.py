from django import forms
from models import WorkSheet,Product, Member
import datetime

class UploadWorkSheetForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

    class Meta:
        fields = ('title', 'file',)
        model = WorkSheet

class UploadWorkSheetForm2(forms.ModelForm):
    name = forms.CharField(max_length=30)
    price=forms.DecimalField(max_digits=8,decimal_places=2)
    description= forms.CharField(widget = forms.Textarea)
    photo = forms.FileField()
    class Meta:
        fields = ( 'name', 'price', 'description','photo')
        model = Product

class RegisterForm(forms.Form):
    username = forms.CharField(min_length=3, max_length=15, required=True)
    password = forms.CharField(min_length=3, max_length=15, required=True)
    password1 = forms.CharField(min_length=3, max_length=15, required=True)
    name = forms.CharField(min_length=3, max_length=30, required=True)
    email = forms.EmailField(max_length=40, required=True)

    def __init__(self,request=None, *args,**kwargs):
        super(RegisterForm,self).__init__(*args, **kwargs)
        self.request=request

    def clean_username(self):
        data = self.cleaned_data['username']
        try:
            existuser=Member.objects.filter(username__exact=data)
        except:
            existuser=None
        if existuser:
            self.add_error('username', 'username already exist')
        return data

    def clean(self):
        password = self.cleaned_data.get('password')
        password1 = self.cleaned_data.get('password1')

        if password != password1:
            self.add_error('password','password does not match')
            self.add_error('password1','password does not match')
        return self.cleaned_data

