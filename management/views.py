from django.shortcuts import render
from django.views.generic import FormView
from .forms import StudentForm
from .models import Management
from django.db.models import Q

# Create your views here.
def home(request):
	obj = Management.objects.all()
	query = request.GET.get('q')
	if query:
		obj = Management.objects.filter(student_id__icontains = query)

	context = {
		'student' : obj
	}
	return render(request,"home.html",context)


def add_student(request,*args,**kwargs):
	form = StudentForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = StudentForm()

	context = {
		'form' : form
	}
	return render(request,"add_student.html",context)


def about(request):
	return render(request,"about.html",{})


	
