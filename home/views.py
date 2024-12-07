from django.shortcuts import render, redirect
from datetime import datetime
from .forms import NewMessageForm
from .models import Messages

def index(request):
    messages = Messages.objects.all()
    return render(request, 'home/index.html', {'messages': messages})

def new(request):
    if request.method == 'POST':
        print('yesss')
        form = NewMessageForm(request.POST)  
        if form.is_valid(): 
            print('noo')
            name = form.cleaned_data['name']  
            message = form.cleaned_data['message'] 
            Messages.objects.create(user=name, text=message)
        else:
            print("Form errors:", form.errors) 
        return redirect('index')  
    else:
        form = NewMessageForm()

    return render(request, 'home/new.html', {'form': form})
