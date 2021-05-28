from django import forms


class ContactUsForm(forms.Form):
	sender_name = forms.CharField(widget=forms.TextInput())
	email_to = forms.CharField(widget=forms.EmailInput())
	sender_message = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}))
