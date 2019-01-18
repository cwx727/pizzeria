from django import forms
from .models import Pizza, Topping


class PizzaForm(forms.ModelForm):
	class Meta:
		model = Pizza
		fields = ['name']   #models.Pizza中的字段
		labels = {'name':''}
		
		
class ToppingForm(forms.ModelForm):
	class Meta:
		model = Topping
		fields = ['name']   #models.Pizza中的字段
		labels = {'name':''}
		widgets = {'name': forms.Textarea(attrs={'cols': 80})}

