from django import forms
from .models import Comment


class ContactUsForm(forms.Form):
	sender_name = forms.CharField(widget=forms.TextInput())
	email_to = forms.CharField(widget=forms.EmailInput())
	sender_message = forms.CharField(widget=forms.Textarea(attrs={'rows': 8}))

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text', 'id']