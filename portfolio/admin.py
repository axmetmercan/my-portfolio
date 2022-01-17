from django.contrib import admin
from django.db import models

from portfolio.models import AboutMe, Categories, Hobbie, Project, Resume, Study, WorkExperience, myportfolio

from .models import  ProjectImage

# Register your models here.
admin.site.register(myportfolio)
admin.site.register(AboutMe)
admin.site.register(Study)
admin.site.register(Hobbie)
admin.site.register(WorkExperience)
admin.site.register(Resume)
admin.site.register(Categories)



class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines =[
        ProjectImageAdmin,
    ]

    list_display = ('title', 'git_link')
    list_display_links = ['title', 'git_link']
    list_filter = ['public_date', 'category']
    search_fields = ['title', 'description']

    class Meta:
        model = Project



