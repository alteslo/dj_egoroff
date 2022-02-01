from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.http import HttpResponseRedirect
from django.urls import reverse

from collections import namedtuple


Type_zodiac = namedtuple('Type_zodiac', 'type zodiacs')
fire = Type_zodiac('fire', ['aries', 'leo', 'sagittarius'])
earth = Type_zodiac('earth', ['taurus', 'virgo', 'capricorn'])
air = Type_zodiac('air', ['gemini', 'libra', 'aquarius'])
water = Type_zodiac('water', ['cancer', 'scorpio', 'pisces'])

elements = [fire, earth, air, water]


# Create your views here.
def get_info_about_zodiac_sign(request, sign_zodiac: str):
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
    data = {
        'info_zodiac': sign
    }
    if sign:
        return render(request, r'horoscope\main_info.html', context=data)
    else:
        return HttpResponseNotFound(f'Такого знака ({sign_zodiac}) нет')


def get_info_about_zodiac_types(request):
    elements_url_li = ''
    for element in elements:
        elements_url_li += f'<li><a href="{element.type}">{element.type.capitalize()}</a></li>'
    elements_url = f'<ul>{elements_url_li}</ul>'
    return(HttpResponse(elements_url))


def get_info_about_element_zodiac(request, element):
    dict_elements = {el.type: el.zodiacs for el in elements}
    element_zodiacs = dict_elements.get(element)
    url_li = ''
    if element_zodiacs is not None:
        for zodiac in element_zodiacs:
            url = reverse("info-sign", args=(zodiac, ))
            url_li += f'<li><a href="{url}">{zodiac.capitalize()}</a></li>'
        return HttpResponse(f'<ul>{url_li}</ul>')
    else:
        return HttpResponseNotFound(f'Такого элемента {element} нет')


def get_info_about_my_zodiac(request, month, day):
    Zodiac = namedtuple('Zodiacs', 'date sign')
    zodiac_info = {
        (3, 4): Zodiac({3: (21, 31), 4: (1, 20)}, 'aries'),
        (4, 5): Zodiac({4: (21, 30), 5: (1, 20)}, 'taurus'),
        (5, 6): Zodiac({5: (21, 31), 6: (1, 21)}, 'gemini'),
        (6, 7): Zodiac({6: (21, 30), 7: (1, 22)}, 'cancer'),
        (7, 8): Zodiac({7: (21, 31), 8: (1, 22)}, 'leo'),
        (8, 9): Zodiac({8: (21, 31), 9: (1, 22)}, 'virgo'),
        (9, 10): Zodiac({9: (21, 30), 10: (1, 22)}, 'libra'),
        (10, 11): Zodiac({10: (21, 31), 11: (1, 21)}, 'scorpio'),
        (11, 12): Zodiac({11: (21, 30), 12: (1, 20)}, 'sagittarius'),
        (12, 1): Zodiac({12: (21, 31), 1: (1, 19)}, 'capricorn'),
        (1, 2): Zodiac({1: (21, 31), 2: (1, 19)}, 'aquarius'),
        (2, 3): Zodiac({2: (21, 29), 3: (1, 20)}, 'pisces')
    }
    if month in range(1, 13):
        for monthes in zodiac_info.keys():
            if month in monthes:
                zodiac = zodiac_info.get(monthes)
                first, last = zodiac.date.get(month)
                if day in range(first, last + 1):
                    redirect_url = reverse('info-sign', args=(zodiac.sign, ))
                    return HttpResponseRedirect(redirect_url)
                else:
                    return HttpResponseNotFound(f'Проверь день {day}')
    else:
        return HttpResponseNotFound(f'Проверь месяц {month}')
