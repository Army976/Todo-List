from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def about(request):
	context = {'first_name': 'Army', 'last_name': 'Hope'}
	return render(request, 'about.html', context)
