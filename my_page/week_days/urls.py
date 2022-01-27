from django.urls import path

from . import views


urlpatterns = [
    path('<int:num_day>', views.today_day),
    path('<str:week_day>', views.week_days_list_to_do, name='number-day')
]
