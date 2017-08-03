from django import forms
from .models import Developer, Templates
from  django.forms import Textarea

class DeveloperForm(forms.ModelForm):
	"""docstring for DeveloperForm"""
	class Meta:
		model = Developer
		fields = '__all__'

		widgets = {
			'bio': Textarea(attrs = {'cols':40, 'rows': 15 })
		}

		labels = {
			'name': 'Name',
			'age' :	'Age',
			'bio' : 'Biography',
			'especiality': 'Especiality', 
			'picture' : 'Picture',
			'email' : 'Email',
			'curriculum' : 'C.V.',
		}

choicestxt=(('col-md-7','col-md-7'),('col-md-7 col-md-push-5','col-md-7 col-md-push-5'))
choicesimg=(('col-md-5','col-md-5'),('col-md-5 col-md-pull-7','col-md-5 col-md-pull-7'))

class TemplateForm(forms.ModelForm):

	
	class Meta:
		model= Templates
		fields = '__all__'

		widgets = {
			'description': Textarea(attrs = {'cols':40, 'rows': 15}),
			'dtex': forms.Select(attrs={'class':'form-control'}, choices=choicestxt),
            'dimg': forms.Select(attrs={'class':'form-control'}, choices=choicesimg),
		}

		labels = {
			'name': 'Name',
			'description': 'Description', 
			'developer': 'Developer',
			'url': 'Url',
			'picture':'Picture',
			'dtex': 'Div Text',
            'dimg': 'Div Img',
		}
	
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    widgets = {
            'message': Textarea(attrs={'cols': 20, 'rows': 15})
        }