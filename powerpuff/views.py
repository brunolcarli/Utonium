from django.shortcuts import render

def index(request):
	"""Homepage"""
	return render(request, 'powerpuff/index.html')
