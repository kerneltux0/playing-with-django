from django.shortcuts import render
from .models import Testing

# Create your views here.
def testing_detail_view(request):
    obj = Testing.objects.get(id=1)
    context = {
        'title': obj.title,
        'info': obj.info,
        'coolStuff': obj.coolStuff
    }
    
    return render(request, "testing/detail.html", {})