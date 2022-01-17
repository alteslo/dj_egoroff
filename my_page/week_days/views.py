from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def week_days_list_to_do(request, week_day):
    week_days_to_do_list = {
        'monday': [1, 2, 3],
        'tuesday': [4, 5, 6],
        'wednesday': [7, 8, 9],
        'thursday': [10, 11, 12],
        'friday': [13, 1, 3],
        'saturday': [14, 15, 2],
        'sunday': [16, 6, 8]
    }
    to_do_list = week_days_to_do_list.get(week_day)
    if to_do_list is not None:
        to_do = '\n'.join(map(str, to_do_list))
        return HttpResponse(to_do)
    else:
        return HttpResponseNotFound('Такого дня недели не существует')


def today_day(request, week_day: int):
    num_day_numbers = (1, 2, 3, 4, 5, 6, 7)
    if week_day in num_day_numbers:
        return HttpResponse(f'Сегодня {week_day} день недели')
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {week_day}')
