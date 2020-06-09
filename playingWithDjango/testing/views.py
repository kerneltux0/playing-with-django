from django.shortcuts import render
from .models import Testing
from .forms import TestForm

# Create your views here.

def testing_create_view(request):
    form = TestForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TestForm()

    context = {
        'form': form
    }


    return render(request, "testing_create.html", context)

def dynamic_lookup_view(request, id):
    obj = Testing.objects.get(id=id)
    context = {
        'object': obj
    }

    return render(request, 'testing_detail.html', context)

def testing_detail_view(request):
    obj = Testing.objects.get(id=1)

    context = {
        'object': obj
    }

    return render(request, "testing_detail.html", context)