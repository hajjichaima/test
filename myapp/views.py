# myapp/views.py

from django.http import HttpResponse

def simple_message(request):
    return HttpResponse("Hello, this is a simple message!")
