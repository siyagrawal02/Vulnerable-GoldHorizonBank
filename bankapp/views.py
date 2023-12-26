
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Account,User
from django.urls import reverse
from datetime import date
from django.views.decorators.cache import *

# Create your views here.
def age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

def login(request):
    template=loader.get_template('try.html')
    return HttpResponse(template.render())

def namelist(request):
    template=loader.get_template('success.html')
    if request.method=="POST":
        prefix=request.POST.get('prefix','none')
        fname=request.POST["Fname"]
        mname=request.POST["Mname"]
        lname=request.POST["Lname"]
        gender=request.POST.get('gender','none')
        father_name=request.POST.get('Father','none')
        mother_name=request.POST.get('Mother','none')
        ph=request.POST.get('Phone','none')
        day=request.POST.get('day')
        month=request.POST.get('month')
        year=request.POST.get('Year')
        a=int(age(date(int(year),int(month),int(day))))  
        email=request.POST.get('email id','none')
        add1=request.POST['line1']
        add2=request.POST['line2']
        state=request.POST['state']
        city=request.POST['city']
        pin=request.POST.get('Pincode','0')
        aadhar=request.POST.get('aadhar','0')
        pan=request.POST.get('pan','12345678')
        
        info=Account(prefix=prefix,fname=fname,mname=mname,lname=lname,gender=gender,father_name=father_name,mother_name=mother_name,phone=ph,day=day,month=month,Year=year,age=a,email=email,add1=add1,add2=add2,state=state,city=city,pin=pin,aadhar=aadhar,pan=pan)
        
        info.save()
        
        return HttpResponse(template.render())
     
    return render(request,"cust.html")



def signup(request):
    if request.method == 'POST':
        # Get the form data from the request object
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        phone=request.POST.get('phone')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Insert the form data into the database using a model
        
        user = User(firstname=firstname, lastname=lastname, phone=phone, username=username, password=password)
        user.save()

        return HttpResponse('Thanks for signing up!')
    
    return render(request,"signup.html")

def loginpage(request):
    template=loader.get_template('cust.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        usertype=request.POST.get('type')
        
        try:
            user = User.objects.get(username=username,password=password) 
            id=user.id
            context={
                'id':id
            }
             
            if usertype=='student':
                return redirect('namelist')
            
        except User.DoesNotExist:
            return render(request,'loginpage.html', {'message': 'User does not exist. Please register.'})
    return render(request,'loginpage.html')



def loadid(request):
    return render(request,"giveID.html")

def displaylist(request):
    template=loader.get_template('list.html')
    customers=Account.objects.all().values()
    context={
        'customers':customers
    }
    return HttpResponse(template.render(context,request))
def home(request):
    template=loader.get_template('LOGIN.html')
    return HttpResponse(template.render())
def display(request,id):
    customer=Account.objects.get(id=id)
    template=loader.get_template('card.html')
    context={
        'customer':customer
    }
    return HttpResponse(template.render(context,request))

def delete(request , id):
    customer=Account.objects.get(id=id)
    customer.delete()
    return HttpResponseRedirect(reverse('displaylist'))



def update(request):
    if request.method=="POST":
        id=request.POST.get('id')
        template=loader.get_template('update.html')
        customer=Account.objects.get(id=int(id))
        context={
            'customer':customer
        }
    return HttpResponse(template.render(context,request))

def updateinfo(request,id):
    first=request.POST['Fname']
    mid=request.POST['Mname']
    last=request.POST['Lname']
    phone=request.POST['Phone']
    father_name=request.POST['Father']
    mother_name=request.POST['Mother']
    day=request.POST.get('day')
    month=request.POST.get('month')
    year=request.POST.get('Year')
    a=int(age(date(int(year),int(month),int(day))))  
    email=request.POST['email id']
    customer=Account.objects.get(id=id)
    customer.fname=first
    customer.mname=mid
    customer.lname=last
    customer.father_name=father_name
    customer.mother_name=mother_name
    customer.phone=phone
    customer.email=email
    customer.day=day
    customer.month=month
    customer.Year=year
    customer.age=a
    customer.save()
    return HttpResponseRedirect(reverse('displaylist'))

def option(request):
    template=loader.get_template('option.html')
    return HttpResponse(template.render())