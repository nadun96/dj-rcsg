import datetime
from django.shortcuts import render
from .models import new_user
# Create your views here.


def login(request):
    context = {
        'title': 'success'
    }
    return render(request, 'login/login.html', context)


def register(request):
    context = {
        'title': 'unsuccess'
    }
    return render(request, 'login/signup.html', context)


def action_register(request):
    if request.method == "POST":
        student_name = request.POST.get('stuname')
        student_birthday = request.POST.get('stubirthday')
        student_photo = request.FILES['stuphoto']
        student_gemail = request.POST.get('stugemail')
        student_grade = request.POST.get('stugrade')
        student_class = request.POST.get('stuclass')
        student_regdate = datetime.date.today
        student_entrance = request.POST.get('stuentrance')
        student_residance = request.POST.get('sturesidance')
        student_guardian = request.POST.get('stuguardian')
        student_gtele = request.POST.get('stugtele')
        student_gemail = request.POST.get('stugemail')
        student_mother = request.POST.get('stumother')
        student_mothertele = request.POST.get('stumothertele')
        student_otherskills = request.POST.get('stuotherskills')
        student_certificate = request.FILES['stucertificate']
        student_letter = request.FILES['stuletter']
        student_medical = request.FILES['stumedical']
        student_sports = request.POST.get('stusports')
        student_password = request.POST.get('stupassword')

        # new_user create
        nu = new_user.objects.create(
            student_name=student_name,
            email=student_gemail,
            student_birthday=student_birthday,
            student_regdate=student_regdate,
            student_photo=student_photo,
            student_gemail=student_gemail,
            student_grade=student_grade,
            student_class=student_class,
            student_entrance=student_entrance,
            student_residance=student_residance,
            student_guardian=student_guardian,
            student_gtele=student_gtele,
            student_mother=student_mother,
            student_mothertele=student_mothertele,
            student_otherskills=student_otherskills,
            student_certificate=student_certificate,
            student_letter=student_letter,
            student_medical=student_medical,
            student_sports=student_sports, student_password=student_password)

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
