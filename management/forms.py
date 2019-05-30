from django import forms
from .models import Management

class StudentForm(forms.ModelForm):
	class Meta:
		model = Management
		fields = [
			'student_id',
			'image',
			'first_name',
			'last_name',
			'father_name',
			'mother_name',
			'Present_address',
			'Permanent_address',
			'contact',
			'avg_cgpa',
]