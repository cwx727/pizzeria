from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse   #新加
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import PizzaForm, ToppingForm   #新加

# Create your views here.
def index(request):
	return render(request, 'pizzas/index.html')

@login_required	
def pizzas(request):
	pizzas = Pizza.objects.filter(owner=request.user).all()
	context = {'pizzas':pizzas}
	return render(request, 'pizzas/pizzas.html', context)

@login_required	
def pizza(request,pizza_id):
	pizza = Pizza.objects.get(id=pizza_id)
	if pizza.owner != request.user:
		raise Http404
	
	topping = pizza.topping_set.all()
	context = {'pizza':pizza, 'toppings':topping}
	return render(request, 'pizzas/pizza.html', context)

@login_required	
def new_pizza(request):
	if request.method != 'POST':
		form = PizzaForm()
	else:
		form = PizzaForm(request.POST)
		if form.is_valid():
			new_pizza = form.save(commit=False)
			new_pizza.owner = request.user
			new_pizza.save()
			return HttpResponseRedirect('/pizzas')
	context = {'form':form}
	return render(request, 'pizzas/new_pizza.html',context)

@login_required	
def new_topping(request,pizza_id):
	pizza = Pizza.objects.get(id = pizza_id)
	
	if request.method != 'POST':
		form = ToppingForm()
	else:
		form = ToppingForm(request.POST)
		if form.is_valid():
			new_topping = form.save(commit=False)
			new_topping.pizza = pizza
			new_topping.save()
			return HttpResponseRedirect('/pizzas/%s'%pizza_id)
			#return HttpResponseRedirect(reverse('pizzas:pizza',args=[pizza_id]))
	context = {'pizza':pizza, 'form':form}
	return render(request, 'pizzas/new_topping.html',context)

@login_required	
def edit_topping(request,topping_id):
	topping = Topping.objects.get(id = topping_id)
	pizza = topping.pizza
	if pizza.owner != request.user:
		raise Http404
	
	if request.method != 'POST':
		form = ToppingForm(instance=topping)
	else:
		form = ToppingForm(instance=topping,data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/pizzas/%s'%pizza.id)
			#return HttpResponseRedirect(reverse('pizzas:pizza',args=[pizza_id]))
	context = {'topping':topping, 'pizza':pizza, 'form':form}
	return render(request, 'pizzas/edit_topping.html',context)	

	
