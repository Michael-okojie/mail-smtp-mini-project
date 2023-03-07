from django.urls import path

from .views import ContactFormView, SuccessView

app_name = 'mail'

urlpatterns = [
	path('', ContactFormView.as_view(), name='contact_us'),
	path('success/', SuccessView.as_view(), name='success')
]
