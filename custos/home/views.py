from django.shortcuts import render
from django.template import RequestContext
# Create your views here.

def hello_world(request):
    """
    basic method
    """
    return render(request, 'home/home.html')

def handler404(request, exception, template_name="404.html"):
    response = render(None, template_name)
    response.status_code = 404
    return response