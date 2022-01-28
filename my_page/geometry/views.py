from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

import math
# Create your views here.


def get_rectangle_area(request, width, height):
    square = width * height
    return HttpResponse(f'<b>Площадь прямоугольника размером {width}х{height} равна {square}</b>')


def get_square_area(request, width):
    square = width ** 2
    return HttpResponse(f'<b>Площадь квадрата размером {width}х{width} равна {square}</b>')


def get_circle_area(request, radius):
    square = int(math.pi * radius ** 2)
    return HttpResponse(f'<b>Площадь круга 3.14*{radius}^2 равна {square}</b>')


# Fuction with reverse
def rectangle_area(request, width, height):
    redirect_url = reverse('rectangle-name', args=(width, height))
    return HttpResponseRedirect(redirect_url)


def square_area(request, width):
    redirect_url = reverse('square-name', args=(width, ))
    return HttpResponseRedirect(redirect_url)


def circle_area(request, radius):
    redirect_url = reverse('circle-name', args=(radius, ))
    return HttpResponseRedirect(redirect_url)
