from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField

# Create your models here.

class myportfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Name', )
    surname = models.CharField(max_length=150, verbose_name = 'Surname')
    picture = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    me = models.ForeignKey(myportfolio, on_delete=CASCADE, verbose_name = "Programmer")
    about_me = models.TextField(max_length=1000, null= False, blank= False, verbose_name= "About Me")
    study = models.TextField(max_length=1000, null= False, blank= False, verbose_name= "Study")
    work_experiences = TextField(max_length=1000, null= False, blank= False, verbose_name= "Work Experiences")
    hobbies = TextField(max_length=1000, null= False, blank= False, verbose_name= "Hobbies")

