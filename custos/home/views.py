from django.shortcuts import render

# Create your views here.

def hello_world(request):
    """
    basic method
    """
    return render(request, 'home/home.html')
