from django.shortcuts import render
from django.shortcuts import HttpResponse
from news.forms import MomentForm
import os


def index(request):
    return render(request,'news\index.html')
def moments_input(request):
    if request.method=='POST':
        form=MomentForm(request.POST)
        if form.is_valid():
            moment=form.save()
            moment.save()
            return render(request,'news\index.html')
    else:
        form=MomentForm()
    PROJECT_ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return render(request,os.path.join(PROJECT_ROOT,'news\\templates','moments_input.html'),{'form':form})


# Create your views here.
