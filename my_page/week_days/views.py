from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse


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
        return render(request, 'week_days/greeting.html')
    else:
        return HttpResponseNotFound('Такого дня недели не существует')


def today_day(request, num_day: int):
    week_days = [
        'monday', 'tuesday', 'wednesday', 'thursday',
        'friday', 'saturday', 'sunday'
        ]

    if num_day in range(1, 8):
        day = week_days[num_day - 1]
        redirect_url = reverse('number-day', args=(day, ))
        return HttpResponseRedirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Неверный номер дня - {num_day}')
