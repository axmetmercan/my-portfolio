
from unicodedata import category
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404,reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from portfolio.models import AboutMe, Categories, Hobbie, Project, Resume, Study, WorkExperience, myportfolio

# Create your views here.
def index(request):
    if request.method == 'GET':
        try:
            personal = myportfolio.objects.get()
        except:
            personal = None
        context = {
            "personal": personal,
        }
        print(context.get("personal"))


    return render(request, 'personal.html', context)

def whoami(request):
    try:
        about_me = AboutMe.objects.get()
    except:
        about_me = None
    study = Study.objects.all()
    work_experiences = WorkExperience.objects.all()
    hobbies = Hobbie.objects.all()
    resumes = Resume.objects.all()

    context = {
        "about_me":about_me,
        "studies":study,
        "workexperiences": work_experiences,
        "hobbies":hobbies,
        "resumes":resumes
    }

    return render(request, "whoami.html", context)

def my_projects(request):



    projects = Project.objects.all().order_by('-public_date')
    categories = Categories.objects.all()
    page = request.GET.get("page",1)
    paginator = Paginator(projects, 1)

    try:
        all_projects = paginator.page(page)
    except PageNotAnInteger:
        all_projects = paginator.page(1)
    except EmptyPage:
        all_projects = paginator.page(paginator.num_pages)



    context = {
        "projects" : all_projects,
        "categories":categories,
    }
    return render(request, 'myprojects.html', context)


def my_projects_with_cat(request, arg):

    catcegory = Categories.objects.filter(name = arg.replace("-", " ").lower().title())
    projects = Project.objects.filter(category = catcegory[0])

    page = request.GET.get("page",1)
    paginator = Paginator(projects, 1)

    try:
        all_projects = paginator.page(page)
    except PageNotAnInteger:
        all_projects = paginator.page(1)
    except EmptyPage:
        all_projects = paginator.page(paginator.num_pages)



    context = {
        "category": catcegory[0],
        "projects":all_projects,
    }
   
    
    return render(request, "myprojects.html", context)

def details(request, id):

    project = Project.objects.get(id = id)

    context = {
        'project':project
    }
    return render(request, 'details.html',context)