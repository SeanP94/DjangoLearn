from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import CustomerForm
# Create your views here.

def addnew(request):
    if request.method == 'POST':
        formset = CustomerForm(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect("/")
    else:
        formset = CustomerForm()
        return render(request, 'addnew.html', {'formset' : formset})


def home(request):
    return render(request, 'index.html')