
from django.shortcuts import redirect, render, HttpResponse, get_object_or_404,reverse

# Create your views here.
def index(request):
    return render(request, 'index.html')