```
||||||||||  |||     ||| ||||||\\\    ///|||\\\  ||\\   //||
|||     \\\ |||     ||| |||   |||   ///     \\\ |||\\ //|||
|||     /// |||     ||| |||   ///   |||     ||| ||| ||| |||
||||||||||  |||     ||| ||||||||||| |||     ||| |||     |||
|||\\\      |||     ||| |||     ||| |||     ||| |||     |||
||| \\\     |||     ||| |||     ||| |||     ||| |||     |||
|||  \\\    \\\     /// |||     /// \\\     /// |||     |||
|||   \\\    \\\|||///  ||||||||||   \\\|||///  |||     |||
```
## Content

- [About the new version](https://github.com/Maxython/RUBOM/releases/tag/v0.1.1)
- [What is RUBOM](#What-is-RUBOM)
- [Installation](#Installation)
- [Commands](#Commands)
  - [Add](#Add)
  - [Choose](#Choose)
    - [Sms](#Sms)
  - [Return](#Return)
    - [Pol](#Pol)
    - [Bomber](#Bomber)
    - [Sel](#Sel)
  - [Set](#Set)
    - [Driver selection](#Driver-selection)
    - [Headless mode](#Headless-mode)
    - [Window size](#Window-size)
    - [Add ip (proxy)](#Add-ip-(proxy))
    - [Chrome driver installer](#Chrome-driver-installer)
  - [Start](#Start)
  - [Supplements](#Supplements)
    - [Clear](#Clear)
    - [Version (v)](#Version-(v))
    - [Exit](#Exit)
    - [Help](#Help)
- [Launch stages](#Launch-stages)

## What is RUBOM
RUBOM - a bomber jacket for Russian numbers with Russian numbers. The program itself is completely Russian, except for the team. Hint: it is possible that the next updates will include not only Russian numbers :blush:

## Installation
To install and run RUBOM, you need to clone and run `rubom.py`.  
RUBY is supported on the most recent version of python (3.9).
```
$git clone https://github.com/Maxython/RUBOM
$cd RUBOM
$python3 rubom.py
```
The missing modules will be automatically installed.

## Commands
All teams are English.

- ### Add
   The command to add a victim (user). To do this, you need a number, email, first name, last name and patronymic (everything except the number is optional).  
   **Example:**
   ```
   command>add 89999999999 email@gmail.com Иван Иванович Иванович
   
   Номер об этом россияне был сохранён.
   
   command>
   ```
   If you want to enter the victim's name, but don't remember the email. You can specify ***none*** in the email line.  
   **Example:**
   ```
   command>add 89999999999 none Иван Иванович Иванович
   
   Номер об этом россияне был сохранён.
   
   command>
   ```
- ### Choose
   The command to select the bomber.  
   **Example:**
   ```
   command>choose
   
   Пора выбирать бумбер, это всё sms)
   
   1-банк тинькофф(sel)
   2-банк санкт-петербург(sel)
   3-мтс(req)
   4-теле(sel)
   5-выход

   choice>
   ```
   Next to the bomber options, there will be brackets with the module that will be used.  
   **sel** - through the ***selenium*** module.  
   **req** - through the ***requests*** module.  
   **What does this mean?**  
   This means that if you use RUBOM on ***Termux***, then bombers that work through selenium will not work!  
   - #### Sms
      Bomber method that sends a certain number of SMS (the number of messages must be specified in the [start](#Start) command).  
      **Note** :heavy_exclamation_mark:: 1 of the bomber method will work with a certain ***operator***.  
      Method ***3***, you need a ***mts operator***.
- ### Return
   A command that returns all information about the victim, the selected bomber and driver settings for Selenium.  
   **Example:**
   ```
   command>return

   Вот вся информация:{'bomber': {'type': 4, 'url': 'https://msk.tele2.ru/tariffs'}, 'pol': {'number': '89999999999', 'email': 'email@gmail.com', 'name': 'Иван', 'surname': 'Иванович', 'patronymic': 'Иванович', 'connection': 'megafon'}}.

   command>
   ```
   You can also return specific information.  
   - #### Pol
      Returns information about the victim.  
      **Example:**
      ```
      command>return pol

      Вот вся информация:{'number': '89999999999', 'email': 'email@gmail.com', 'name': 'Иван', 'surname': 'Иванович', 'patronymic': 'Иванович', 'connection': 'megafon'}.

      command>
      ```
   - #### Bomber
      Returns information about the bomber.  
      **Example:**
      ```
      command>return bomber

      Вот вся информация:{'type': 4, 'url': 'https://msk.tele2.ru/tariffs'}.

      command>
      ```
   - #### Sel
      Returns configuration information for Selenium.  
      **Example:**
      ```
      command>return sel

      Вот вся информация:{'type': 'chrome', 'headless': True, 'window_size': '1920x935', 'proxy': None, 'installer_chrome_win': True}.

      command>
      ```
- ### Set
   This command enables the setting for selenium.  
   **Example:**
   ```
   command>set
   
   Уверен ты знаешь что делать.
   1-выбор драйвера
   2-безголовый режим
   3-размер окна
   4-добавить ip(прокси)
   5-установщик драйвера chrome
   6-выход

   choice>
   ```
   - #### Driver selection
      Department for driver selection.  
      There are 2 choices. These are ***Chrome*** and ***FireFox***.  
      The default is ***Chrome***.  
      **Example:**
      ```
      choice>1
      
      1-chrome
      2-firefox
      3-выход

      choice>
      ```
      For the program to work, you need a specific webdriver, the program itself will give a link to download it. But for every opportunity, I left them here.  
      - [Webdriver for Chrome.](https://chromedriver.chromium.org/downloads)
      - [Webdriver for FireFox.](https://github.com/mozilla/geckodriver/releases/)
   - #### Headless mode
      Department for turning on and off the opening window(headless mode) during the operation of the bomber.
      The default is ***True***.  
      **Example:**
      ```
      choice>2
      
      1-True
      2-False
      3-выход
      
      choice>
      ```
   - #### Window size
      Department for indicating the size of the window when the bomber is launched.  
      The default is ***1920x935***.  
      **Example:**
      ```
      choice>3
      
      Укажите размер окна драйвера, через пробел(1-выход).

      value>
      ```
      First you need to specify the ***height***, then the ***width***, separated by a space.  
      **Example:**
      ```
      value>1920 935
      ```
   - #### Add ip (proxy)
      Department by ip (proxy).  
      **Example:**
      ```
      choice>4
      
      Укажите прокси, c http или типо того(1-выход, none-неуказан).
      
      value>
      ```
      The proxy must have the type specified, to remove the proxy, enter ***none***.  
      **Example:**  
      ```
      value>http://213.111.230.247:8080
      ```
   - #### Chrome driver installer
      Department for enabling or disabling the driver installer for Chrome.  
      This feature is only available for Windows users.  
      The default value depends on the OS, Windows is **True**, something else is **False**. 
      **Example:**
      ```
      choice>5
      
      1-True
      2-False
      3-выход
      
      choice>
      ```
- ### Start
   The command that launches the bomber.  
   Before launching the bomber, it will ask for the number of future sms sent to the victim.  
   **Example:**
   ```
   command>start
   
   Введи количество будущих отправленных sms(не больше 100).
   
   quantity>
   ```
   The number must be no more than 100.
- ### Supplements
   - #### Clear
      Command to clear the screen.  
      **Example:**
      ```
      command>clear
      ```
   - #### Version (v)
      Command that returns the version of the program.  
      **Example:**
      ```
      command>v
      
      0.1
      ```
   - #### Exit
      The command to exit the program.  
      **Example:**
      ```
      command>exit
      
      Пока, уверен мы ещё увидимся.
      ```
   - #### Help
      Help team.  
      **Example:**
      ```
      command>help
      ```
## Launch stages
To launch the bomber, you need to go through 3 stages.  
1. Add a victim using the [**add**](#Add) command.
2. Select the method of bombers using the [**choose**](#Choose) command.
3. Start the bomber with the [**start**](#Start) command.  

That's all.
