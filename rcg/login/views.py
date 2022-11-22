from django.shortcuts import render

# Create your views here.

def login(request):
    context = {
        'title': 'login',
    }
    return render(request, 'login/login.html', context)



def register(request):
    context = {
        'title': 'register',
    }
    return render(request, 'login/signup.html' , context)