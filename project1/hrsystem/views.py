from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def home (request):
    return HttpResponse ("HR system home page")
    #return render(request,'hrsystem.html')

def contact (request):
    return HttpResponse ("Contact with hr team")