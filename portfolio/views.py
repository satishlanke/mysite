from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.mail import EmailMessage





# Create your views here.


def index(request):
    if request.method == "POST":
        name=request.POST['name']
        u_email = request.POST['email']
        phone=request.POST['phone']
        message = request.POST['message']
        to_email = ["satishlanke31@gmail.com"]
        print(name)
        print(to_email)
        email = EmailMessage(subject='MAIL_FROM Web Portfolio',body=name+u_email+phone+message,to=to_email)
        email.send()
        thanq="THANK YOU FOR VISITING"
        return render(request,'index.html',{'thanq':thanq})
    return render(request,'index.html')


