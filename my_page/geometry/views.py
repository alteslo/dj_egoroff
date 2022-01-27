from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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


def rectangle_area(request, width, height):
    return HttpResponseRedirect(f'/calculate_geometry/rectangle/{width}/{height}')


def square_area(request, width):
    return HttpResponseRedirect(f'/calculate_geometry/square/{width}')


def circle_area(request, radius):
    return HttpResponseRedirect(f'/calculate_geometry/circle/{radius}')
