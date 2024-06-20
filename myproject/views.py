# from django.http import HttpResponse
from django.shortcuts import render
def homepage(request):
    # return HttpResponse("Hello world, I'm in home")
    return render(request,'home.html')

def aboutpage(request):
    # return HttpResponse("Hello world,now I'm in about")
    return render(request,'about.html')