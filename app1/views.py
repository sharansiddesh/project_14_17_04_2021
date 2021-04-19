from django.shortcuts import render

# Create your views here.
def page1(request):
    return render(request,'1.html', context={"name":"sharansiddesh",'age':23,'email':'sharansiddesh99@gamil.com'})


def page2(request):
    return render(request,'2.html')


def page3(request,data,age1,email1):
    return render(request,'3.html', context={'name':data,'age1':age1,'email1':email1})