from django.shortcuts import render

# Create your views here.

def Log_in(request):
    return render(request, "log_in.html")
