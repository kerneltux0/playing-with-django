from django.shortcuts import render
from .models import Testing
from .forms import TestForm

# Create your views here.

def testing_create_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': obj
    }


    return render(request, "testing_detail.html", context)

def testing_detail_view(request):
    obj = Testing.objects.get(id=1)

    context = {
        'object': obj
    }
    # context = {
    #     'title': obj.title,
    #     'info': obj.info,
    #     'coolStuff': obj.coolStuff
    # }

    return render(request, "testing_detail.html", context)