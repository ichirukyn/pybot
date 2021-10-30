# import telebot
# import requests
# from bs4 import BeautifulSoup
# import urllib.request
# import json
# import re

# url = 'https://jut.su/anime/'
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36'}
# anime_dict = dict()
# anime_user_dict = dict()
# anime_series_dict = dict()
# anime_season_dict = dict()
# num = 1
# new_url = '/one-piece/'
# a_name = 'Ван пис'


# def anime_list(url,headers):
# 	for num in range(2):
# 		response = requests.post(url, headers=headers, data = {'start_from_page': num})
# 		soup = BeautifulSoup(response.text, 'lxml')
# 		name = soup.find_all(class_="aaname")

# 		for anime in name:
# 		    href = anime.find_parent("a")['href']
# 		    anime_dict[anime.get_text()] = href
# 		num = num + 1
# 		# print(anime_dict)
# 	return soup

# anime_list(url,headers)

# def anime_season(url,headers):
# 	i = 1
# 	new_url = "https://jut.su" + url
# 	response = requests.post(new_url, headers=headers)
# 	soup = BeautifulSoup(response.text, 'lxml')
# 	number = soup.find_all(class_="the-anime-season")
# 	# print(number)

# 	for x in number:
# 		anime_season_dict[str(x.get_text()).split(' ')[0]] = x.get_text()
# 		i = i + i
		
# 	# print(anime_season_dict)
# 	return anime_season_dict


# anime_season(new_url, headers)


# def anime_series(url, headers, a_name, u_season):
# 	new_url = "https://jut.su" + url

# 	if u_season != 0:
# 		season_name = a_name + " " + u_season
# 	else:
# 		season_name = a_name

# 	response = requests.post(new_url, headers=headers)
# 	soup = BeautifulSoup(response.text, 'html.parser')
# 	number = soup.find_all("a",class_="the_hildi")
# 	seasons = soup.find(string=season_name)

# 	for series in number:
# 		# if season_name != series.i.get_text():
# 		if season_name.replace(' ', '').lower() == series.i.get_text().replace(' ', '').lower():
# 			anime_series_dict[re.split(',', series.get_text(","))[-1]] = series['href']
# 	# print(anime_series_dict)
# 	return season_name
# anime_series(new_url, headers, 'Ван пис', 0)

# u_series = '222'
# in_series = 15
# i = 0

# for ser in anime_series_dict.keys():
# 	if str(ser) == str(u_series) + ' серия':
# 		if in_series != 0:
# 			while i <= in_series:	
# 				anime_user_dict[str(u_series) + ' серия'] = anime_series_dict.get(str(u_series) + ' серия')
# 				u_series = int(u_series) + 1
# 				i += 1
# 		else:
# 			u_series = anime_series_dict.get(ser)
			

# print(anime_user_dict)


# def save(url, headers, anime_user_dict, in_series, u_series, a_name):

# 	if in_series != 0:
# 		for key,value in anime_user_dict.items():
# 			new_url = "https://jut.su" + value
# 			response = requests.get(new_url, headers=headers)

# 			soup = BeautifulSoup(response.text, 'lxml')
# 			quotes = soup.source

			
# 			if str(quotes) == "None":
# 				print('Аниме заблокировано в России')
# 			else:
# 				if in_series != 0:
# 					dwn_link = quotes['src']
# 					opener = urllib.request.build_opener()
# 					opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
# 					urllib.request.install_opener(opener)
# 					urllib.request.urlretrieve(dwn_link, a_name + key +'.mp4') 
# 					print("Установка " + a_name + key +'.mp4' + " : Успешно")
# 	else:
# 		new_url = "https://jut.su" + u_series
# 		response = requests.get(new_url, headers=headers)

# 		soup = BeautifulSoup(response.text, 'lxml')
# 		quotes = soup.source

		
# 		if str(quotes) == "None":
# 			print('Аниме заблокировано в России')
# 		else:
# 			if in_series == 0:
# 				dwn_link = quotes['src']
# 				opener = urllib.request.build_opener()
# 				opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')]
# 				urllib.request.install_opener(opener)
# 				urllib.request.urlretrieve(dwn_link, a_name + u_series +'.mp4') 

# save(url, headers, anime_user_dict, in_series, u_series, a_name)
# import pyautogui
# import keyboard
# import time
# import random

# def _sendMouseEvent(ev, x, y, dwData=0):
#     assert x != None and y != None, 'x and y cannot be set to None'
#     width, height = _size()
#     convertedX = 65536 * x // width + 1
#     convertedY = 65536 * y // height + 1
#     ctypes.windll.user32.mouse_event(ev, ctypes.c_long(convertedX), ctypes.c_long(convertedY), dwData, 0)

# i = 0
# time.sleep(3)
# while True:

# 	print(i)

# 	if i == 2:
# 		break
# 	i = i + 1

# 	pos = pyautogui.position()
# 	# a = random.random()
# 	# pyautogui.click(interval=a)
# 	print(pos[0], pos)

# 	_sendMouseEvent()


# 	# if keyboard.is_pressed('ctrl'):
# 		# pyautogui.click()
# 		# print('Нажата клавиша: a')

from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class AnimateGifLabel(Label):
    def __init__(self, *argv, image = None,  **kwargs):
        self.master = argv[0]
        self.filename = image
        self.check_cadrs()
        self.i = 0
        self.img = Image.open(image)
        self.img.seek(0)
        self.image = ImageTk.PhotoImage(self.img)
        super().__init__(*argv, image = self.image, **kwargs)
        if 'delay' in kwargs:
            self.delay = kwargs['delay']
        else:
            try:
                self.delay = self.img.info['duration']
            except:
                self.delay = 100
        self.delay = 1000 # Это минимально возможная задержка - иначе ткинтер не успевает обновится и не обновляет 2  (Но реагирует на события типа изменнения размера ) а при 1 даже не появляется
        self.after(self.delay, self.show_new_cadr)


    def check_cadrs(self):
        self.cadrs = Image.open(self.filename).n_frames
    def show_new_cadr(self):
        if self.i == self.cadrs:
            self.i=0
        self.img.seek(self.i)
        self.image = ImageTk.PhotoImage(self.img)
        self.config(image = self.image)
        self.i+=1
        self.master.after(self.delay, self.show_new_cadr)


class VideoLabel(Label):
    def __init__(self, *argv, video = None,  **kwargs):
        self.master = argv[0]
        self.filename = video
        self.video = cv2.VideoCapture(self.filename)
        cap = VideoFileClip(self.filename)
        audio = cap.audio
        audio.write_audiofile('$-python-tk-video-frame-audio.wav')
        pygame.init()
        self.sound = pygame.mixer.Sound('$-python-tk-video-frame-audio.wav')
        #clip = VideoFileClip(self.filename)
        #clip.write_gif("$~python-tk-video-label.gif")
        #self.filename = "$~python-tk-video-label.gif"
        flag, frame = self.video.read()
        self.image = self.tk_image(frame)
        super().__init__(*argv, image = self.image, text = '0 sec', compound = 'top',  **kwargs)
        self.sound.play()
        self.after(35, self.show_new_cadr)
        self.i=1
    def tk_image(self, cvframe):
        cv2.imwrite("$-python-tk-video-frame.jpg", cvframe)
        img = Image.open("$-python-tk-video-frame.jpg")
        return ImageTk.PhotoImage(img)
    def show_new_cadr(self):
        self.i+=1
        flag, frame = self.video.read()
        if flag == False:
            self.i = 0
            self.video.set(0, 0)
        self.image = self.tk_image(frame)
        self.config(image = self.image, text = str(self.i//24) + ' sec')
        self.master.after(35, self.show_new_cadr)



root = Tk()
root.title('Tkinter gif')
root['bg'] = 'white'
AnimateGifLabel(root, image = filedialog.askopenfilename(filetypes = (('GIF Animation Image', '*.gif'),('All files', '*.*')))).pack()
# clipka = VideoLabel(root,  video  = filedialog.askopenfilename(filetypes=(('MP4 Video', '*.mp4'),('All files', '*.*'))))
# clipka.pack( expand =1 , fill = 'both')
root.mainloop()
