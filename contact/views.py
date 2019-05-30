from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm


# Create your views here.

def contact(request,*args,**kwargs):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ContactForm()

	context = {
		'form' : form
	}
	return render(request,"contact.html",context)