from django.shortcuts import render
# from django.http import Httpresponse

def homepage (request):
    context={
    "msg":"Hello World!"
    }
    return render(request,"home.html",context)
