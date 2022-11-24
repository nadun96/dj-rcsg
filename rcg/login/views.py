import datetime
from django.shortcuts import render
from .models import new_user
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
    return render(request, 'login/signup.html', context)


def action_register(request):
    if request.method == "POST":
        stuname = request.POST.get('stuname')
        stubirthday = request.POST.get('stubirthday')
        stuphoto = request.FILES['stuphoto']
        stugemail = request.POST.get('stugemail')
        stugrade = request.POST.get('stugrade')
        stuclass = request.POST.get('stuclass')
        sturegdate = datetime.date.today
        stuentrance = request.POST.get('stuentrance')
        sturesidance = request.POST.get('sturesidance')
        stuguardian = request.POST.get('stuguardian')
        stugtele = request.POST.get('stugtele')
        stugemail = request.POST.get('stugemail')
        stumother = request.POST.get('stumother')
        stumothertele = request.POST.get('stumothertele')
        stuotherskills = request.POST.get('stuotherskills')
        stucertificate = request.FILES['stucertificate']
        stuletter = request.FILES['stuletter']
        stumedical = request.FILES['stumedical']
        stusports = request.POST.get('stusports')
        stupassword = request.POST.get('stupassword')

        # new_user create
        nu = new_user.objects.create(stuname=stuname, stubirthday=stubirthday, sturegdate=sturegdate, stuphoto=stuphoto, stugemail=stugemail, stugrade=stugrade, stuclass=stuclass, stuentrance=stuentrance, sturesidance=sturesidance, stuguardian=stuguardian,
                                     stugtele=stugtele, stumother=stumother, stumothertele=stumothertele, stuotherskills=stuotherskills, stucertificate=stucertificate, stuletter=stuletter, stumedical=stumedical, stusports=stusports, stupassword=stupassword)

        # new_user save to database
        nu.save()

        context = {'title': 'register-success'}
        return render(request, 'login/signup.html', context)
    else:
        context = {'title': 'register-success'}
        return render(request, 'login/signup.html', context)


def action_login(request):
    # CHECK REQUEST METHOD
    if request.method == "POST":

        # save user_name password in variables
        uname = request.POST.get('username')
        password = request.POST.get('password')

        # check if user_name and password are correct
