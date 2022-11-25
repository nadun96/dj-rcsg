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
    email = models.CharField(max_length=100)
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

    def __str__(self):
        return self.email

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
# model for user manager
##
class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


##
# model for custom user
##

class Account(AbstractBaseUser):

    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    Account_photo = models.ImageField(
        upload_to=get_photo_filepath, null=True, blank=True, default=get_deafult_photo)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = MyAccountManager()

    USER_NAME = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.user.username

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module(self, app_label):
        return True

    def get_photo_filename(self, filename):
        return str(self.Account_photo)[str(self.Account_photo).index(f'photos/{self.pk}/'):]
