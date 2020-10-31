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

- [What is RUBOM](#What-is-RUBOM)
- [Commands](#Commands)
  - [Add](#Add)
  - [Choose](#Choose)
    - [Sms](#Sms)
    - [Calls](#Calls)
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
  - [Clear](#Clear)

## What is RUBOM
RUBOM - a bomber jacket for Russian numbers with Russian numbers. The program itself is completely Russian, except for the team. Hint: it is possible that the next updates will include not only Russian numbers :blush:

## Commands
All teams are English.

- ### Add
   The command to add a victim (user). To do this, you need a number, first name, last name and patronymic (the latter is optional).  
   **Example:**
   ```
   command>add 89999999999 Иван Иванович Иванович
   
   Номер об этом россияне был сохранён.
   
   command>
   ```
- ### Choose
   The command to select the bomber. There are only 2 types: ***1*** - SMS and ***2*** - call.  
   **Example:**
   ```
   command>choose
   
   Пора выбирать бумбер)
   1-sms сообщения
   2-звонки
   3-выйти
   
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
      Method ***2***, you need a ***mts operator***.
   - #### Calls
      A bomber method that makes a call for a victim.
- ### Return
   A command that returns all information about the victim, the selected bomber and driver settings for Selenium.  
   **Example:**
   ```
   command>return

   Вот вся информация:{'pol': {'number': '89999999999', 'name': 'Иван', 'surname': 'Иванович', 'patronymic': 'Иванович', 'connection': 'megafon'}, 'bomber': {'type1': 1, 'type2': 1, 'url': 'https://www.instagram.com/accounts/emailsignup/?hl=ru'}}.

   command>
   ```
   You can also return specific information.  
   - #### Pol
      Returns information about the victim.  
      **Example:**
      ```
      command>return pol

      Вот вся информация:{'number': '89999999999', 'name': 'Иван', 'surname': 'Иванович', 'patronymic': 'Иванович', 'connection': 'megafon'}.

      command>
      ```
   - #### Bomber
      Returns information about the bomber.  
      **Example:**
      ```
      command>return bomber

      Вот вся информация:{'type1': 1, 'type2': 1, 'url': 'https://www.instagram.com/accounts/emailsignup/?hl=ru'}.

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
      **Example:**
      ```
      choice>1
      
      1-chrome
      2-firefox
      3-выход

      choice>
      ```
      For the program to work, you need a specific webdriver, the program itself will give a link to download it. But for every opportunity, I left them here.  
      Webdriver for Chrome.  
      Webdriver for FireFox.  
   - #### Headless mode
   - #### Window size
   - #### Add ip (proxy)
   - #### Chrome driver installer
- ### Start
- ### Clear
