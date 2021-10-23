


from django.db.models import indexes
from django.urls.conf import path
from . import views 


app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name="index"),
]