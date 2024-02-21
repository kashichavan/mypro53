from django.shortcuts import render
from .forms import TrainerForm

# Create your views here.

def home(request):
    if request.method=="POST":
        form=TrainerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
    f=TrainerForm()
    return render(request,'home.html',context={'form':f})
