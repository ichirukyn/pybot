import telebot
import requests
from bs4 import BeautifulSoup
import urllib.request
import json
import re

url = 'https://jut.su/anime/'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
anime_dict = dict()
anime_user_dict = dict()
anime_series_dict = dict()
anime_season_dict = dict()
num = 1
new_url = '/one-piece/'
a_name = 'Ван пис'


def anime_list(url,headers):
	for num in range(2):
		response = requests.post(url, headers=headers, data = {'start_from_page': num})
		soup = BeautifulSoup(response.text, 'lxml')
		name = soup.find_all(class_="aaname")

		for anime in name:
		    href = anime.find_parent("a")['href']
		    anime_dict[anime.get_text()] = href
		num = num + 1
		# print(anime_dict)
	return soup

anime_list(url,headers)

def anime_season(url,headers):
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


anime_season(new_url, headers)


def anime_series(url, headers, a_name, u_season):
	new_url = "https://jut.su" + url

	if u_season != 0:
		season_name = a_name + " " + u_season
	else:
		season_name = a_name

	response = requests.post(new_url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	number = soup.find_all("a",class_="the_hildi")
	seasons = soup.find(string=season_name)

	for series in number:
		# if season_name != series.i.get_text():
		if season_name.replace(' ', '').lower() == series.i.get_text().replace(' ', '').lower():
			anime_series_dict[re.split(',', series.get_text(","))[-1]] = series['href']
	# print(anime_series_dict)
	return season_name
anime_series(new_url, headers, 'Ван пис', 0)

u_series = '222'
in_series = 15
i = 0

for ser in anime_series_dict.keys():
	if str(ser) == str(u_series) + ' серия':
		if in_series != 0:
			while i <= in_series:	
				anime_user_dict[str(u_series) + ' серия'] = anime_series_dict.get(str(u_series) + ' серия')
				u_series = int(u_series) + 1
				i += 1
		else:
			u_series = anime_series_dict.get(ser)
			

print(anime_user_dict)


def save(url, headers, anime_user_dict, in_series, u_series, a_name):

	if in_series != 0:
		for key,value in anime_user_dict.items():
			new_url = "https://jut.su" + value
			response = requests.get(new_url, headers=headers)

			soup = BeautifulSoup(response.text, 'lxml')
			quotes = soup.source

			
			if str(quotes) == "None":
				print('Аниме заблокировано в России')
			else:
				if in_series != 0:
					dwn_link = quotes['src']
					opener = urllib.request.build_opener()
					opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
					urllib.request.install_opener(opener)
					urllib.request.urlretrieve(dwn_link, a_name + key +'.mp4') 
					print("Установка " + a_name + key +'.mp4' + " : Успешно")
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
				opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
				urllib.request.install_opener(opener)
				urllib.request.urlretrieve(dwn_link, a_name + u_series +'.mp4') 

save(url, headers, anime_user_dict, in_series, u_series, a_name)