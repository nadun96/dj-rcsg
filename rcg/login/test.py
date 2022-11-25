from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, is_staff=False, is_admin=False, is_active=True):

        if phone is None:
            raise TypeError('Users must have a phonenumber.')

        user = self.model(phone=phone)
        user.set_password(password)
        user.staff = is_staff
        user.admin = is_admin
        user.active = is_active
        user.save(using=self._db)

        return user


def create_staffuser(self, phone, password):
    """
    Creates and saves a staff user with the given email and password.
    """
    user = self.create_user(
        phone,
        password=password,
        is_staff=True
    )
#    user.staff = True
    user.save(using=self._db)
    return users


def create_superuser(self, phone, password):
    """
    Creates and saves a superuser with the given email and password.
    """
    user = self.create_user(
        phone=phone,
        password=password,
        is_staff=True,
        is_admin=True
    )
    #user.staff = True
    #user.admin = True
    # user.active=True
    user.save(using=self._db)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(
        regex=r'^[6-9]\d{9}$', message='please enter the correct phonenumber')

    #name_regex=RegexValidator(regex=r'/^[A-Za-z]+$/',message='Please enter the correct name')
    phone = models.CharField(validators=[phone_regex], max_length=15, unique=True)
    name = models.CharField(max_length=15)
    date_joined = models.DateTimeField(
        verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)  # a admin user; non super-user
    admin = models.BooleanField(default=False)
    first_login = models.BooleanField(default=False)

USERNAME_FIELD = 'phone'
REQUIRED_FIELDS = []


objects = UserManager()


def __str__(self):

    return self.phone


@property
def token(self):

    return self._generate_jwt_token()


def get_full_name(self):

    return self.name


def has_perm(self, perm, obj=None):

    return True


def has_module_perms(self, app_label):

    return True


# Below is code of serializer.py


class RegistrationSerializer(serializers.ModelSerializer):


    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )


    token = serializers.CharField(max_length=255, read_only=True)


    class Meta:

        fields = ['phone', 'password']


    def create(self, validated_data):

        return User.objects.create_user(**validated_data)
