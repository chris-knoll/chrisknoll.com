from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, 'main/home.html')

def resume(request):
	return render(request, 'main/resume.html')

def projects(request):
	return render(request, 'main/projects.html')

def contact(request):
	return render(request, 'main/contact.html')