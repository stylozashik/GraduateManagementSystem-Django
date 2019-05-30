from django import forms
from .models import contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = contact
		fields = [
			'Name',
			'Email',
			'Message',
]