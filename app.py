from PIL import Image,ImageGrab
import pytesseract
# import pywhatkit as kt
import pyautogui as pg
import time
import os
import urllib.request
import requests
from PIL import Image
import re
from bs4 import BeautifulSoup
import youtube_dl
# import HTMLParser
# from autoscraper import Autoscraper

def get_video_url(name):
	try:
		url =f"https://www.youtube.com/results?search_query={name.replace(' ','+')}+full+audio"
		soup = BeautifulSoup(requests.get(url).content,'html.parser').prettify()
		# print(soup.find_all('script'))
		link = soup.split('{"videoId":"')[1]
		link = link.split('","thumbnail"')[0]
		video_url = f'https://www.youtube.com/watch?v={link}'
		return video_url 
	except:
		print(f'skipped {name}')
def download(video_url):
	try:	
		video_info = youtube_dl.YoutubeDL().extract_info(
		url = video_url,download=False
		)
		filename = f"{video_info['title']}.mp3"
		options={
		'format':'bestaudio/best',
		'keepvideo':False,
		'outtmpl':f'music/{filename}',
		}
		with youtube_dl.YoutubeDL(options) as ydl:
			ydl.download([video_info['webpage_url']])
		# print(filename)
	except:
		print('not able to download')
 
	print("Download complete... {}".format(filename))



def main():
	# test.png => location_of_image
		# path =f""
	for j in range(int(len(os.listdir('pics')))):
		img = Image.open("pics/{}.jpg".format(j+1))
		# img.show()
		w,h = img.size

		for i in range(9):
			if 190*(i+1)>h:
				print("size wali bhackchodi")
				break
			im = img.crop((0,190*i,w,190*(i+1)))
			# im.show()
			name = pytesseract.image_to_string(im, lang="eng")
			print(name)
			video_url = get_video_url(name)
			download(video_url)

if __name__ =='__main__':
	main()

# html = urllib.request.urlopen(f)
# # print(html.read().decode())
# video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
# print(video_ids[1])

# name='lalala y2k'

# url =f"https://www.youtube.com/results?search_query={name.replace(' ','+')}"
# soup = BeautifulSoup(requests.get(url).content,'html.parser').prettify()
# # print(soup.find_all('script'))
# link = soup.split('{"videoId":"')[1]
# link = link.split('","thumbnail"')[0]


# wanted_list =["N2Y2vQ-1m7M"]
# scraper = Autoscraper()
# result=scraper.build(url,wanted_list)









# import youtube_dl

# # # help(youtube_dl)

# video_url = f'https://www.youtube.com/watch?v={link}'
# video_info = youtube_dl.YoutubeDL().extract_info(
# url = video_url,download=False
# )
# filename = f"{video_info['title']}.mp3"
# options={
# 'format':'bestaudio/best',
# 'keepvideo':False,
# 'outtmpl':filename,
# }
# with youtube_dl.YoutubeDL(options) as ydl:
# 	ydl.download([video_info['webpage_url']])


# print("Download complete... {}".format(filename))
















