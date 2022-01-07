from django.urls import path

from . import views


urlpatterns = [
    path('leo/', views.leo),
    path('scorpio/', views.scorpio),
    path('aries/', views.aries),
    path('taurus/', views.taurus),
    path('gemini/', views.gemini),
    path('cancer/', views.cancer),
    path('virgo/', views.virgo),
    path('libra/', views.libra),
    path('sagittarius/', views.sagittarius),
    path('capricorn/', views.capricorn),
    path('aquarius/', views.aquarius),
    path('pisces/', views.pisces),
]
