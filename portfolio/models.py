from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import F
from django.db.models.fields import CharField, DateTimeField, TextField
from django.contrib.auth.models import User
from django.db.models.fields.files import FileField, ImageField
from django.db.models.fields.related import ForeignKey, ForeignObject

# Create your models here.

class myportfolio(models.Model):
    name = models.CharField(max_length=100, verbose_name = 'Name', )
    surname = models.CharField(max_length=150, verbose_name = 'Surname')
    picture = models.ImageField(upload_to = "images/")
    github = models.CharField(max_length=250, verbose_name="Git link")
    bitbucket = models.CharField(max_length=250, verbose_name="BitBucket Link")
    linkedin = models.CharField(max_length=250, verbose_name="Linkedin")
    fb = models.CharField(max_length=250, verbose_name="Facebook")
    instagram = models.CharField(max_length=250, verbose_name="Instagram Link")

    def __str__(self):
        return self.name

class AboutMe(models.Model):
    about_me = models.TextField(max_length=1000, null= False, blank= False, verbose_name= "About Me")


class Study(models.Model):
    primary_school = models.CharField(max_length=1000, null= False, blank= False, verbose_name= "Study")
    high_school = models.CharField(max_length=1000, null= False, blank= False, verbose_name= "High School Name")
    bachelor_degree = models.CharField(max_length=1000,  null= False, blank= False, verbose_name= "University Name and Department")

    def __str__(self) :
        return "School Names"

class WorkExperience(models.Model):
    company = TextField(max_length=1000, null= False, blank= False, verbose_name= "Work Experiences")
    position = TextField(max_length=100, verbose_name="Position at that job", null=False, blank=False)
    start_date = DateTimeField(verbose_name="Job Start Date", null=False, blank=False)
    end_date = DateTimeField(verbose_name="Job End Date", null=True, blank=True)

    def __str__(self) -> str:
        return self.company

class Hobbie(models.Model):
    hobbies = CharField(max_length=1000, null= False, blank= False, verbose_name= "Hobbies")

    def __str__(self) :
        return self.hobbies


class Resume(models.Model):
    resume_name = CharField(max_length=100, verbose_name="Resume Name", null=False, blank=False)
    qr_code_pic = ImageField(upload_to="cv/", verbose_name="Image Field")
    link = CharField(max_length=255)

    def __str__(self):
        return self.resume_name


class Categories(models.Model):
    name = CharField(max_length=150, null=False, blank=False, verbose_name="Category Name")

    def __str__(self):
        return self.name


class Project(models.Model):
    category = models.ForeignKey(Categories, on_delete= models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.FileField(blank=True)
    git_link = models.CharField(max_length = 255, blank=True, null= True)
    public_date = models.DateTimeField(auto_now_add=True, verbose_name="Publication Date")

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-public_date"]

class ProjectImage(models.Model):
    project = ForeignKey(Project, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')

    def __str__(self):
        return self.title

