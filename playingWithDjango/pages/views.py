from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        'my_text': 'Take a guess',
        'this_num': 3.14
    }
    return render(request, "home.html", my_context)
    
def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})