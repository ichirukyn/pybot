# Все функции
import function


# Стандартный url
url = 'https://jut.su'
# Заголовок, чтобы попасть на сайт
headers = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36',
'accept': '*/*'
}
# Токен, для подключения бота
token = "844679093:AAFP0FZivx1tmlEmC25aLYaFCWxRbNtjoC0"



# Словари, на которых всё держится
# Общий список, названий и ссылок на аниме
anime_dict = dict()
# Словарь, со всеми сериями выбранными пользователем
anime_user_dict = dict()
# Общий список, названий и ссылок на серии
anime_series_dict = dict()



# Пользовательский ввод
# print("Введите название Аниме")
# anime_name_input = input()

# print("Введите сезон")
# anime_season_input = input()

# print("Введите серию")
# anime_series_input = input()

# print("Колличество серий")
# anime_in_series_input = input()

anime_name_input = "Ван пис"
anime_season_input = 0
anime_series_input = 1
anime_in_series_input = 1


# Присваиваем словарю данные из функции anime_list
anime_dict = function.anime_list(url, headers, anime_name_input)
# Присваиваем словарю данные из функции anime_series
anime_series_dict = function.anime_series(url, headers, anime_series_input, anime_season_input, anime_dict,anime_in_series_input)
# Сохраняем нужную серию
function.save_anime(url, headers, anime_series_dict, anime_in_series_input, anime_dict)