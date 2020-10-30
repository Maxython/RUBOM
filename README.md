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
      Bomber method that sends a certain number of SMS (the number of messages must be specified in the launch command).  
      **Note** :heavy_exclamation_mark:: 1 of the bomber method will work with a certain ***operator***.  
      Method ***2***, you need a ***mts operator***.
   - #### Calls
      A bomber method that makes a call for a victim.
- ### Return
- ### Set
- ### Start
- ### Clear
