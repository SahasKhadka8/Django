from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
from .form import *

def myhome(request):
    return HttpResponse("This is home page")

def myfunc(request):
    return HttpResponse("This is about page")

def add(request,a,b):
    return HttpResponse(a+b)

def mul(request,a,b,c):
    return HttpResponse(a*b*c)

def Arko(request,name,age):
    mydict={
        "Name":name,
        "Age":age
    }
    return JsonResponse(mydict)


def Feri(request,address,phonenumber):
    myphone={
        "Address":address,
        "PhoneNumber":phonenumber
    }
    return JsonResponse(myphone)

def Again(request,name,age,address,phoneno):
    detail={
        "Name":name,
        "Age":age,
        "Address":address,
        "Phone Number":phoneno,
    }
    return JsonResponse(detail)


def firstpage(request):
    return render(request,'first.html')

def secondpage(request):
    return render(request,'second.html')

def thirdpage(request):
    var='Hello'
    greeting='How are you'
    fruits=['Mango','Banana','Apple','Grapes','Orange']
    students=['Cr','Jhusey','Sabin Sir','Bhusal']
    num1,num2=10,8
    ans=num1>num2
    dict={
        'var':var,
        'greet':greeting,
        'myfruits':fruits,
        'clzz':students,
        'num1':num1,
        'num2':num2,
        'ans':ans,

        
    }

    return render(request,'third.html',context=dict)


def imagepage(request):
    return render(request,'imagepage.html')


def formpage(request):
    return render(request,'myform.html')

def myform(request):
    dict1={
        'Name':request.GET['name'],
        'Password':request.GET['pass'],
        'Submit':request.GET['sub'],
        'Method':request.method
    }
    return JsonResponse(dict1)

def myform2(request):
    form= FeedbackForm()
    mydict={
        'form':form
    }
    return render(request,'myform2.html',context=mydict)

def submitform(request):
    sub={
        'Title':request.GET['title'],
        'Subject':request.GET['subject']
    }
    return JsonResponse(sub)

def error_404_view(request,exception):
    return render(request,'404.html')

