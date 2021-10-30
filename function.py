# библиотека для запросов
import requests
# Парсер
from bs4 import BeautifulSoup  
# Для перезаписи в файл
import urllib.request 
# Для обработки текста
import re
import progressbar
import os
# from telethon import TelegramClient, sync

# полезные переменные, потом уберу
num = 1
pbar = None

# Прогресс бар из telethon
def callback(current, total):
    print('Uploaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))

# Прогресс бар к urllib
def show_progress(block_num, block_size, total_size):
    global pbar
    if pbar is None:
        pbar = progressbar.ProgressBar(maxval=total_size)
        pbar.start()

    downloaded = block_num * block_size
    if downloaded < total_size:
        pbar.update(downloaded)
    else:
        pbar.finish()
        pbar = None

# Самая гланая функция, ищет аниме на сайте
def anime_list(url, headers, anime_name_input):
    anime_dict = dict()
    # На случай, если аниме не найдено, чтобы не ловить ошибку пустой переменной.
    anime_check = False
    # Перебор всех страниц с аниме на сайте
    for num in range(30):
        # Запросить нужную страницу, поправляем, чтобы попасть куда надо..
        response = requests.post(url + "/anime/", headers=headers, data={'start_from_page': num})
        # Переводим в полученные данные в формат BeautifulSoup, с которым удобно работать
        soup = BeautifulSoup(response.text, 'lxml')
        # Находим необходимую информацию, заносим в массив
        anime_name = soup.find_all(class_="aaname")

        # Перебор всего массива в поисках нужного аниме
        for name in anime_name:
            # Сам поиск аниме, убирает пробелы и переводит в нижний формат для "точного" сравнения
            if name.get_text().replace(' ', '').lower() == anime_name_input.replace(' ', '').lower():
                # Ссылка на аниме
                href = name.find_parent("a")['href']
                # Заносим информацию в словарь
                anime_dict[name.get_text()] = href
                # Заглушка, которая сработает после нахожджения аниме.
                anime_check = True
                # Оповещения пользователя о прогрессе
                print("Аниме нашел, выдвигаюсь!")
                # Остановка перебора нижнего цикла
                break

        # Заглушка и остановка верхнего цикла
        if anime_check:
            break
        else:
            print("Аниме не найдено :(")
            # Сообщаем интерфейсу, что ничего мы не нашли..
            anime_dict = None
            break
        # Двигатель массива..
        num += 1

    # Возвращаем словарь в main 
    return anime_dict


# Находит серию на странице аниме, которую получили из прошлой функции
def anime_series(url, headers, anime_series_input, anime_season_input, anime_dict, anime_in_series):
    anime_series_dict = dict()

    # Разбираем словарь ...
    for key,value in anime_dict.items():
        # Собираем новый url, для парсинга
        anime_url = str(url) + str(value)

        # Сразу проверка на сезоны
        if anime_season_input == 0:
            # Если сезонов нет, то присваиваем переменной имя аниме
            season_name = key
        else:
            # А если есть, то добавляем сезон, который ищем
            season_name = key + " " + anime_season_input + " сезон"
        break

    # Запрос к старнице с аниме
    response = requests.get(anime_url, headers=headers)
    # Снова переводим в удобный формат
    soup = BeautifulSoup(response.text, 'html.parser')
    # Наводим парсер на ссылку серии
    number = soup.find_all("a", class_="the_hildi")

    # Цикл перебора серий, который находит нужную нам
    for series in number:
        
        # Ищем нужную серию/серии
        if re.split(',', series.get_text(","))[-1] == str(anime_series_input) + " серия":

            # Проверка на существование сезонов
            if anime_season_input == "0":

                # Немного косметики и вносим в словарь, уже и сам не помню что тут происходит..
                anime_series_dict[re.split(',', series.get_text(","))[-1]] = series['href']
                print("Серия найдена!")
                # Не забываем про заглушки, иначе будет очень грустно..

            else:

                # Выбираем нужный сезон
                if season_name.replace(' ', '').lower() == series.i.get_text().replace(' ', '').lower():
                    # Снова косметика
                    anime_series_dict[re.split(',', series.get_text(","))[-1]] = series['href']
                    # Общение с пользователем
                    print("Сезон найден!")
                    break

                else:
                    # Если такой имеется..
                    print("Такого сезона не существует ((")
                    break
            if str(anime_in_series) != '0':
                anime_series_input = int(anime_series_input) + 1
                anime_in_series = int(anime_in_series) - 1     
            else:
                break
    # Возвращаем серии которые хочет пользователь..
    return anime_series_dict

# Главная функция для сохранения серий
def save_anime(url, headers, anime_series_dict, anime_in_series_input, anime_dict):

    # Начинаем с проверки на кол-во серий
    if anime_in_series_input != 0:
    
        # Разбираем словарь, для удобства
        for key, value in anime_series_dict.items():
            
            # Новый url для доступа к серии
            series_url = "https://jut.su" + value
            # Запрос к серии
            response = requests.get(series_url, headers=headers)
            # Переводим страницу в формат..
            soup = BeautifulSoup(response.text, 'lxml')
            # Сразу выбираем нужные данные
            # source - тег html, первый найденный это лучшее качество!
            quotes = soup.source

            # Если source не найден, то аниме заблокировано..
            if str(quotes) == "None":
                # Сообщаем эту пачальную весть пользователю
                print('Аниме заблокировано в России Т.Т')
            
            else:
            
                # Забираем название аниме
                for name in anime_dict.keys():
                    # Всё хорошо, говорим пользователю, чтобы не парился
                    print("Загрузка. Пожалуйста подождите...")


                    print("Установка началась!")
                    dwn_link = quotes['src']
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    
                    # Забираем ссылку из sorce через атрибут src
                    dwn_link = quotes['src']
                    # Если папка не существуем, создаем
                    if not os.path.isdir(name):
                        os.mkdir(name)
                    # Путь куда качается
                    path = name + '/' +name + ' ' + key + '.mp4'
                    # Открываем запрсо через urllib
                    # Дальше творится магия
                    # urllib переписывает файл из ссылки в новый, который можно переместить в любую папку
                    opener = urllib.request.build_opener()
                    # Заголовок, для urllib, ему нужно свои добавлять, по умолчанию они отсутствуют
                    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    # Тут главное выбрать папку и имя файла
                    urllib.request.urlretrieve(dwn_link, path, show_progress)
                    # Докладываем пользователю
                    print("Установка " + path + " : Успешно")
                    # send_telegram(path)
                    # os.remove(path)
                    print(dwn_link)
    
    else:

        # Всё тоже самое, только для одной серии
        for key, value in anime_series_dict.items():
        
            # Собираем ссылку на серию
            series_url = "https://jut.su" + value
            # Запрос за серией
            response = requests.get(series_url, headers=headers)
            # Форматируем
            soup = BeautifulSoup(response.text, 'lxml')
            # Выбираем нужный ресурс
            quotes = soup.source

            # Проверка на доступность в России
            if str(quotes) == "None":
                # Плачем
                print('Аниме заблокировано в России Т.Т')
        
            else:
        
                # Название для серии
                for name in anime_dict.keys():

                    print("Загрузка. Пожалуйста подождите...")
                    # Ссылка из source
                    dwn_link = quotes['src']
                    path = name + ' ' + u_series + '.mp4'
                    # Немного песен с бубном
                    opener = urllib.request.build_opener()
                    opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    # Название для серии (и путь если нужно)
                    urllib.request.urlretrieve(dwn_link, path)
                    print("Установка " + path + " : Успешно")
                    # Отправление в телеграм
                    # send_telegram(path)

# Функция отправления видео в телеграм канал
def send_telegram(path):
    # Вставляем api_id и api_hash (Нужно создать app в телеграм)
    api_id = 6086209
    api_hash = '35bee7a8d0ee8c6f652ea05d8159b068'

    # Инициация клиента
    client = TelegramClient('Ai', api_id, api_hash)
    # Стартуем клиента
    client.start()
    # Связь
    print("Отправляем в телегу!")
    # Отправляем в телеграм
    client.send_file('@One_piece_1080', path, progress_callback=callback)
    print("Успешно отправил!!")