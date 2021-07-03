# библиотека для запросов
import requests
# Парсер
from bs4 import BeautifulSoup  
# Для перезаписи в файл
import urllib.request 
# Для обработки текста
import re
# Все функции
import function

# Стандартный url
url = 'https://jut.su'
# Заголовок, чтобы попасть на сайт
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}

# Словари, на которых всё держится
# Общий список, названий и ссылок на аниме
anime_dict = dict()
# Словарь, со всеми сериями выбранными пользователем
anime_user_dict = dict()
# Общий список, названий и ссылок на серии
anime_series_dict = dict()
# Список сезонов
anime_season_dict = dict()
# полезные переменные, потом уберу
num = 1
i = 1

# Пользовательский ввод
print("Введите название Аниме")
anime_name_input = input()

print("Введите сезон")
anime_season_input = input()

print("Введите серию")
anime_series_input = input()

print("Колличество серий")
anime_in_series_input = input()

# Присваиваем словарю данные из функции anime_list
anime_dict = function.anime_list(url, headers)
print(anime_dict)


for k in anime_dict.keys():
    if k == anime_name:
        new_url = anime_dict.get(k)
        a_name = k
        # print (new_url)

anime_season(new_url, headers)

for r in anime_season_dict.keys():
    if r == u_season:
        u_season = anime_season_dict.get(r)
    elif r == 0:
        u_season = 0


anime_series(new_url, headers, a_name, u_season)

for ser in anime_series_dict.keys():
    if str(ser) == str(u_series) + ' серия':
        if in_series != 0:
            while int(i) <= int(in_series):
                anime_user_dict[str(
                    u_series) + ' серия'] = anime_series_dict.get(str(u_series) + ' серия')
                u_series = int(u_series) + 1
                i += 1
        else:
            u_series = anime_series_dict.get(ser)





save(url, headers, anime_user_dict, in_series, u_series, a_name)
