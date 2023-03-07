from django.views.generic import FormView, TemplateView

from .forms import ContactForm


class ContactFormView(FormView):
	template_name = 'mail/main.html'
	form_class = ContactForm
	success_url = 'success'

	def form_valid(self, form):
		form.send_email()
		return super().form_valid(form)


class SuccessView(TemplateView):
	template_name = 'mail/success.html'
