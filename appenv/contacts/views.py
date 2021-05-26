
from django.shortcuts import render
from .models import Contact
from .forms import SaveContact

def index(request):
    contacts = Contact.objects
    if request.method == 'POST':
       form = SaveContact(request.POST)
       if form.is_valid():
         form.save()
    return render(request,'index.html',{'contacts': contacts})
