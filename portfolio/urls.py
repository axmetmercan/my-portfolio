


from django.db.models import indexes
from django.urls.conf import path
from . import views 


app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name="layout"),
    path("myprojects/", views.my_projects, name="myprojects"),
    path("myprojects/<str:arg>", views.my_projects_with_cat, name = "myprojects1"),
    path("whoami/", views.whoami, name="whoami"),
    path('details/<int:id>',views.details, name='details'),
    
]