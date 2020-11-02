from sys import platform
from os import system
from random import randint, choice
from datetime import datetime

eng_rus_a = {
'а':'a',
'б':'b',
'в':'v',
'г':'g',
'д':'d',
'е':'e',
'ё':'iu',
'ж':'zch',
'з':'z',
'и':'i',
'й':'ie',
'к':'k',
'л':'l',
'м':'m',
'н':'n',
'о':'o',
'п':'p',
'р':'r',
'с':'s',
'т':'t',
'у':'y',
'ф':'sch',
'х':'h',
'ц':'ch',
'ч':'csh',
'ш':'sh',
'щ':'hc',
'ъ':'',
'ы':'ii',
'ь':'i',
'э':'u',
'ю':'iy',
'я':'ia',
' ':'_'
}

name = {
'male':['Александр', 'Богдан', 'Василий', 'Глеб', 'Денис', 'Егор', 'Захар', 'Иван', 'Константин', 'Максим', 'Николай', 'Олег', 'Платон', 'Руслан', 'Cергей', 'Тарас', 'Фёдор', 'Чарли'],
'female':['Алиса', 'Валентина', 'Гелла', 'Диана', 'Елана', 'Жанна', 'Зоя', 'Инна', 'Клара', 'Лариса', 'Мария', 'Надежда', 'Оксана', 'Полина', 'Рита', 'Светлана', 'Татьяна', 'Ульяна', 'Юлия', 'Яна']
}

surname = {
'male':['Алексеев', 'Андреев', 'Антонов', 'Белов', 'Баранов', 'Бобров', 'Волков', 'Васильев', 'Воронов', 'Дашков', 'Дмитриев', 'Демидов', 'Евсеев', 'Жуков', 'Зимин', 'Иванов', 'Калинин'],
'female':['Авдеева', 'Алексеева', 'Афанасьева', 'Безрукова', 'Берия', 'Быкова', 'Вдовина', 'Вавилова', 'Второва', 'Герасимова', 'Голикова', 'Горлова', 'Давыдова', 'Ефимова', 'Жукова', 'Зимина', 'Иванова', 'Казакова']
}

patronymic = {
'male':['Лаврович', 'Ларионович', 'Львович', 'Леонардович', 'Леонтиевич', 'Логвинович', 'Лукич', 'Любимович', 'Маврович', 'Макарович', 'Максимович', 'Маратович', 'Марианович', 'Маркович', 'Мартинович', 'Матвеевич', 'Меркулович', 'Милиевич', 'Миронович', 'Михайлович'],
'female':['Александровна', 'Антоновна', 'Богдановна', 'Валентиновна', 'Валерьевна', 'Виталиевна', 'Вячеславовна', 'Георгиевна', 'Даниловна', 'Денисовна', 'Егоровна', 'Ивановна', 'Иосифовна', 'Леонидовна', 'Максимовна', 'Николаевна', 'Олеговна', 'Павловна', 'Семеновна', 'Станиславна', 'Ярославовна']
}

def eng_rus_name(name):
    text = ''
    for i in name:
        text = text + eng_rus_a[i.lower()]
    return text


def random_password():
    pas = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
    text = ''
    for i in range(randint(10, 20)):
        text = text + pas[randint(1,len(pas))-1]
    return text


def birth(years, str_month=False, title=False, index=False):
    str_mon = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
    time = datetime.now()
    return [time.day, time.month if str_month == False else str_mon[time.month-1] if title == False else str_mon[time.month-1].lower(), time.year-years if index == False else years]


def gen_mail(value=None):
    if value == None:
        pas = 'qwertyuiopasdfghjklzxcvbnm'
        mail = ''
        for i in range(randint(5, 8)):
            mail = mail + pas[randint(0, len(pas)-1)]
        if randint(0, 1) == 1:
            time = datetime.now()
            mail = mail + str(time.year - randint(19, 22))
    else:
        mail = eng_rus_name(value)
    return mail + choice(['@mail.ru', '@gmail.com', '@yandex.ru'])


def gen_name(pyst_patr=False):
    rand = choice(['male', 'female'])
    return [choice(name[rand]), choice(surname[rand]), choice(patronymic[rand]) if randint(0, 4) <= 2 else None if pyst_patr == False else '']


def is_eng(text):
    sl = 'qwertyuiopasdfghjklzxcvbnm'
    ch = '1234567890'
    ch_pr = True
    for i in text:
        if i.lower() in ch:
            if ch_pr == True:
                type = False
        elif i.lower() in sl:
            type = True
            ch_pr = False
        else:
            type = False
    return type


def clear():
    if 'win' in platform:
        system('cls')
    else:
        system('clear')
