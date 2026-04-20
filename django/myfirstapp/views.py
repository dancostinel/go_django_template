from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("<h1>Hello World</h1>")


def home(request):
    context = {
        'name': 'John Doe',
        'age': 30,
        'hobbies': ['Reading', 'Traveling', 'Cooking']
    }

    return render(request, 'myfirstapp/home.html', context)
