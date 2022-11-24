from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

##
# model for New user
##


def get_photo_filepath(self, filename):
    return f'photos/{self.pk}/{"photo.png"}'


def get_deafult_photo():
    return "photos/default.png"


class new_user(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    student_birthday = models.DateField(null=False, Blank=False)
    student_photo = models.ImageField(
        upload_to=get_photo_filepath, null=True, blank=True, default=get_deafult_photo)
    student_gemail = models.EmailField(null=False, Blank=False)
    student_grade = models.IntegerField(max_length=2, null=False, Blank=False)
    student_class = models.CharField(max_length=1)
    student_regdate = models.DateField(
        auto_now_add=True, null=False, Blank=False)
    student_entrance = models.IntegerField(
        max_length=10, null=False, Blank=False)
    student_residance = models.TextField(null=False, Blank=False)
    student_guardian = models.CharField(max_length=200)
    student_gtele = models.IntegerField(null=False, Blank=False)
    student_mother = models.CharField(max_length=200)
    student_mothertele = models.IntegerField(null=True, Blank=True)
    student_otherskills = models.CharField(max_length=200)
    student_certificate = models.FileField(null=False, Blank=False)
    student_letter = models.FileField(null=False, Blank=False)
    student_medical = models.FileField(null=True, Blank=True)
    student_sports = models.CharField(max_length=200, null=True, Blank=True)
    student_password = models.CharField(
        max_length=200, null=False, Blank=False)
    
    # student_id = models.AutoField(
    #     ("auto_user_name"), value=f'{student_name[:2]} {user_id[:5]}')
    # auto_user_name = models.CharField(
    #     max_length=200, default=student_id, editable=True)

    def __str__(self):
        return self.student_name

    def save(self, *args, **kwargs):
        self.student_id = f'{self.student_name[:2]}{super.id[:5]}'.upper()
        super().save(*args, **kwargs)


##
# model for approved user -Member
##


class Member(new_user):
    is_Officer = models.BooleanField(default=False)
    ROLES = ('Secretary', 'Treasurer', 'President', 'Storekeeper')
    role = models.CharField(
        choices=ROLES, default='Member')
    is_Treasurer = models.BooleanField(default=False)
    is_Secretary = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


##
# model for user roles
##
class Account(AbstractBaseUser):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_member = models.BooleanField(default=False)
    is_officer = models.BooleanField(default=False)
    is_treasurer = models.BooleanField(default=False)
    is_secretary = models.BooleanField(default=False)
    is_president = models.BooleanField(default=False)
    is_storekeeper = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


# from django.conf import settings , settings.AUTH_USER_MODEL
# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from django.contrib.auth.models import User
