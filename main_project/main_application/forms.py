#encoding:utf-8 
from django.forms import ModelForm
from django import forms
from main_application.models import Article
#from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

class ContactForm(forms.Form):
	email = forms.EmailField(label='Your e-mail...')
	message = forms.CharField(widget=forms.Textarea)

class ArticleForm(ModelForm):
    class Meta:
        model = Article


# class OtherForm(forms.Form):
	# first_name = forms.CharField(max_length=3, label='Initial\'s of first name')
	# last_name = forms.CharField(max_length=3, label='Initial\'s of last name')
	# date_sur = forms.DateField(label='S date')
	
	# #p = get_object_or_404(Parameter, label='')
	# try:
		# p = Parameter.objects.get(label__iexact='fib_first')
		# fib_first = forms.FloatField(min_value=float(p.min_value), max_value=float(p.max_value),label='fib_first')
	# except ObjectDoesNotExist:
		# print("Doesn't exist.")	
		