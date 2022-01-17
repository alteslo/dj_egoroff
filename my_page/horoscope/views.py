from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from datetime import datetime


# Create your views here.

def get_info_about_zodiac_sign(request, sign_zodiac: str):
    now = datetime.now().strftime("%A, %d %B, %Y at %X")
    sign_zodiac_dict = {
        'leo': 'Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
        'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
        'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
        'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
        'gemini': 'Близнецы- третий знак зодиака,планета Меркурий (с 22 мая по 21 июня).',
        'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
        'virgo': 'Дева - шестой знак зодиака, планета '
                 'Меркурий (с 22 августа по 23 сентября).',
        'libra': 'Весы - седьмой знак зодиака, планета '
                 'Венера (с 24 сентября по 23 октября).',
        'sagittarius': 'Стрелец - девятый знак зодиака, планета '
                       'Юпитер (с 23 ноября по 22 декабря).',
        'capricorn': 'Козерог - десятый знак зодиака, планета '
                     'Сатурн (с 23 декабря по 20 января).',
        'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты '
                    'Уран и Сатурн (с 21 января по 19 февраля).',
        'pisces': 'Рыбы - двенадцатый знак зодиака, '
                  'планеты Юпитер (с 20 февраля по 20 марта).'
    }
    sign = sign_zodiac_dict.get(sign_zodiac)
    if sign:
        return HttpResponse(sign)
    else:
        return HttpResponseNotFound(f'Такого знака ({sign_zodiac}) нет на {now}')
