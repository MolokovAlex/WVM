autor: MolokovAlex
lisence: GPL
coding: utf-8

Программа WebViewMercury - ПО сбора и отображения данных с счетчиков технического учета электроэнергии Меркурий через Web-интерфейс.

Стек:
Python
Django
sqlite3
numpy
serial

12082023_2
исправлены bootstrap.min.css на локальные в папке

12082023_1
12082023
фиксация перед деплоем на VPS

10082023
+ добавлено полое Select в область редактирования счетчиков
- не сделано запись выбранной группы из области реактирования счетчиков

09082023
+ работает форма редактирование состава группы
- нужно здесь сделать распознавание на  update и add

04082023
+ убрали  datepicker
+ сделано в dbpp и dbic  выбор интервала дат

02082023
+ отображени графика на DBIC

27072023
edit_group

26072023
+ редактирование базы счетчиков
- валидация при редактировании
+ страницы добавления счетчика и редактир счетчика объединены

+ {{ item.id }} при нажатии Delete в edit_counter   передаются в форму

22072023
- пока график выводиться средствами chart.js  - ннужно передлать на SVG
+ checkBox в DBIC передаются во вьюху
+ datepicker передается во вьюху
+ выбор счетчика в DBIC передаеться во вьюху

13052023
- фиксация базы 







