# Здесь они тоже нужны..
import requests
from bs4 import BeautifulSoup  

# Самая гланая функия, ищет аниме на сайте
def anime_list(url, headers, anime_name_input):
    # Перебор всех страниц с аниме на сайте
    for num in range(50):
        # Запросить нужную страницу, поправляем, чтобы попасть куда надо..
        response = requests.post(url + "/anime/", headers=headers, data={'start_from_page': num})
        # Переводим в полученные данные в формат BeautifulSoup, с которым удобно работать
        soup = BeautifulSoup(response.text, 'lxml')
        # Находим необходимую информацию, заносим в массив
        anime_name = soup.find_all(class_="aaname")
            
        # Перебор всего массива в поисках нужного аниме
        for name in anime_name:
            # Сам поиск аниме, убирает пробелы и переводит в нижний формат
            if name.replace(' ', '').lower() == anime_name_input.replace(' ', '').lower():
                # Ссылка на аниме
                href = name.find_parent("a")['href']
                # Заносим информацию в словарь
                anime_dict[name.get_text()] = href
                # Заглушка, которая сработает после нахожджения аниме.
                anime_check = true
                # Оповещения пользователя о прогрессе
                print("Аниме нашел, выдвигаюсь!")
                # Остановка перебора нижнего цикла
                break
            else:
                print("Аниме не найдено :(")

        # Заглушка и остановка верхнего цикла
        if anime_check:
            break
        # Двигатель массива..
        num += 1

    # Возвращаем словарь в main 
    return anime_dict


def anime_season(url, headers):
    i = 1
    new_url = "https://jut.su" + url
    response = requests.post(new_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    number = soup.find_all(class_="the-anime-season")
    # print(number)

    for x in number:
        anime_season_dict[str(x.get_text()).split(' ')[0]] = x.get_text()
        i = i + i

    # print(anime_season_dict)
    return anime_season_dict


def anime_series(url, headers, a_name, u_season):
    new_url = "https://jut.su" + url

    if u_season != 0:
        season_name = a_name + " " + u_season
    else:
        season_name = a_name

    response = requests.post(new_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    number = soup.find_all("a", class_="the_hildi")
    seasons = soup.find(string=season_name)

    for series in number:
        # if season_name != series.i.get_text():
        if season_name.replace(' ', '').lower() == series.i.get_text().replace(' ', '').lower():
            anime_series_dict[re.split(
                ',', series.get_text(","))[-1]] = series['href']
    # print(anime_series_dict)
    return season_name


def save(url, headers, anime_user_dict, in_series, u_series, a_name):

    if in_series != 0:
        for key, value in anime_user_dict.items():
            new_url = "https://jut.su" + value
            response = requests.get(new_url, headers=headers)

            soup = BeautifulSoup(response.text, 'lxml')
            quotes = soup.source

            if str(quotes) == "None":
                print('Аниме заблокировано в России')
            else:
                if in_series != 0:
                    print("Загрузка. Пожалуйста подождите...")
                    dwn_link = quotes['src']
                    opener = urllib.request.build_opener()
                    opener.addheaders = [
                        ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
                    urllib.request.install_opener(opener)
                    urllib.request.urlretrieve(
                        dwn_link, a_name + ' ' + key + '.mp4')
                    print("Установка " + a_name + key + '.mp4' + " : Успешно")
    else:
        new_url = "https://jut.su" + u_series
        response = requests.get(new_url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')
        quotes = soup.source

        if str(quotes) == "None":
            print('Аниме заблокировано в России')
        else:
            if in_series == 0:
                dwn_link = quotes['src']
                opener = urllib.request.build_opener()
                opener.addheaders = [
                    ('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
                urllib.request.install_opener(opener)
                urllib.request.urlretrieve(
                    dwn_link, a_name + ' ' + u_series + '.mp4')