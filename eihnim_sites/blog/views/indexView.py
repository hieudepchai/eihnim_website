from django.shortcuts import render
from blog.models import*
# Create your views here.


def index(request):
    list_acc = Account.objects.all()
    return render(request, 'index.html', context=None)
