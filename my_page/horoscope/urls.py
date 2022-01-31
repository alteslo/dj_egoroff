from django.urls import path

from . import views


urlpatterns = [
    path('<int:month>/<int:day>', views.get_info_about_my_zodiac),
    path('type/', views.get_info_about_zodiac_types, name='horo-type'),
    path('type/<element>', views.get_info_about_element_zodiac),
    path('<sign_zodiac>', views.get_info_about_zodiac_sign, name='info-sign')
]
