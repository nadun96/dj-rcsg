from django.db import models
# Create your models here.


#### new user form
# stuname max 200  nn
# stubirthday greater than today nn
# stuphoto nn
# stuemail nn
# stugrade min -5 max -11 nn
# stuclass A-G nn
# sturegdate today nn
# stuentrance nn  number 
# sturesidance nn 
# stuguardian nn 
# stugtele nn
# stugemail nn
# stumother 
# stumothertele
# stuotherskills
# stucertificate nn file
# stuletter nn file
# stumedical file multiple
# stusports 
# stupassword nn
#### new user form



class new_user(models.Model):
    stuname=models.CharField(max_length=200)
    stubirthday=models.DateField()
    stuphoto=models.ImageField()
    stugemail=models.EmailField()
    stugrade=models.IntegerField()
    stuclass=models.CharField(max_length=1)
    sturegdate= models.DateField(auto_now=True, auto_now_add=False)
    stuentrance=models.IntegerField()
    sturesidance=models.TextField()
    stuguardian=models.CharField(max_length=200)
    stugtele=models.IntegerField()
    stugemail=models.EmailField()
    stumother=models.CharField(max_length=200)
    stumothertele=models.IntegerField() 
    stuotherskills=models.CharField(max_length=200)
    stucertificate=models.FileField()
    stuletter=models.FileField()
    stumedical=models.FileField()
    stusports=models.CharField(max_length=200)
    stupassword=models.CharField(max_length=200)
