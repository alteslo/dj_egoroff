from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def monday(request):
    return HttpResponse('список дел на понедельник')


def tuesday(request):
    return HttpResponse('список дел на вторник')
