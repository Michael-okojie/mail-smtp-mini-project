from django import forms
from django.core.mail import send_mail
from django.template.loader import render_to_string


class ContactForm(forms.Form):
	name = forms.CharField(
		max_length=120, widget=forms.TextInput(
			attrs={
				'placeholder': 'Name',
				'style': 'width:300px'
			}
		)
	)
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'style': 'width:300px'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Message', 'style': 'width:300px'}))

	def send_email(self):
		self.name = self.cleaned_data['name']
		self.email = self.cleaned_data['email']
		self.message = self.cleaned_data['message']

		html = render_to_string(
			'mail/success.html', {
				'name': self.name,
				'email': self.email,
				'message': self.message
			}
		)
		send_mail(
			'Contact Us', self.message, self.email, ['okoose03@gmail.com'], html_message=html,
			fail_silently=False
		)
