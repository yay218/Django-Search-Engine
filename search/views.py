from django.shortcuts import render

search = [
	{
		'title': 'Django Search Engine',
	}
]

# Create your views here.
def home(request):
	context = {
		'search': search
	}
	return render(request, 'search/home.html', context)

def about(request):
	return render(request, 'search/about.html', {'title': 'About'})

