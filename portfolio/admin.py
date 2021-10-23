from django.contrib import admin

from portfolio.models import AboutMe, myportfolio

# Register your models here.
admin.site.register(myportfolio)
admin.site.register(AboutMe)