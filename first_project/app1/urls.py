from django.urls import path
from . import views

urlpatterns=[
    path('home',views.myhome,name='Index'),
    path('about',views.myfunc,name='Ind'),
    path('add/<int:a>/<int:b>',views.add,name='add'),
    path('mul/<int:a>/<int:b>/<int:c>',views.mul,name='multiply'),
    path('Arko/<str:name>/<int:age>',views.Arko,name='Arko'),
    path('Feri/<str:address>/<str:phonenumber>',views.Feri,name='Feri'),
    path('J/<str:name>/<int:age>/<str:phoneno>/<str:address>',views.Again,name='I'),
    #views.Again le chai Again vanni method jun views.py mah banaiyethyo tyo call garyo

    path('',views.firstpage,name='I'),
    path('mysecondpage',views.secondpage,name='CR'),
    path('mythirdpage',views.thirdpage,name='Ab'),
    path('myimagepage',views.imagepage,name='image'),
    path('myformpage',views.formpage,name='Fp'),
    path('myform',views.myform,name='sub'),
    path('myform2',views.myform2,name='form'),
    path('myform3',views.submitform,name='submitform2'),
]
