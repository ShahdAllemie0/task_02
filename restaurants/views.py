from django.shortcuts import render
from django.http import Httpresponse

def homepage (request):
    context={
    "msg":"hello CODED!!"
    }
    return render(request,home.html,context)
