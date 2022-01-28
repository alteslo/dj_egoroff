from django.urls import path

from . import views


urlpatterns = [
    path('<sign_zodiac>', views.get_info_about_zodiac_sign),
    path('type/<type>', views.get_info_about_zodiac_types)
]
