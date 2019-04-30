
import pylast
import requests
import hashlib
import vlc
import urllib.request
from bs4 import BeautifulSoup
import pafy
import webbrowser
API_KEY = "46b6ffe5e756a9742b0d7201ecc59a11"
API_SECRET = "d447d7174a48bb04220595eb3dfd94da"
api_head = 'http://ws.audioscrobbler.com/2.0/'
username = "nine_tails9"
password_hash = pylast.md5("donut123@#")

network = pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET,
                               username=username, password_hash=password_hash)
def playSongOnline(emotion):
	textToSearch = 'bollywood '+ emotion + ' song'
	query = urllib.parse.quote(textToSearch)
	url = "https://www.youtube.com/results?search_query=" + query+'&sp=EgIQAw%253D%253D'
	response = urllib.request.urlopen(url)
	html = response.read()
	soup = BeautifulSoup(html, 'html.parser')
	#print(soup)
	for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
		print(vid['href'])
		if '&list=' in vid['href']:
			url = 'https://www.youtube.com/' + vid['href']
			break
	chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
	webbrowser.get(chrome_path).open(url)

def playSongLocal(emotion):
    url1='C:/Users/sk176/Desktop/Study Material/Minor - II/Implementation/songs/' + emotion + '/' + '1.mp3'
    url2='C:/Users/sk176/Desktop/Study Material/Minor - II/Implementation/songs/' + emotion
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url1)
    webbrowser.get(chrome_path).open(url2)

# songs = network.get_tag('energetic')
# print(" ".join(str(x[0]) for x in songs.get_top_albums()))
