import requests
from bs4 import BeautifulSoup
import re

def format_names(band_name, song_name):
    #format the names to match the convention followed by azlyrics URLs
    band_name = band_name.lower()
    song_name = song_name.lower()

    if band_name[:3] == 'the':
        band_name = band_name[4:]
    
    #only alphabets and digtis are allowed
    band_name = re.sub(r'[^a-z0-9]', '', band_name)
    song_name = re.sub(r'[^a-z0-9]', '', song_name)

    return band_name, song_name

def get_webpage(band_name, song_name):
    band_name, song_name = format_names(band_name, song_name)
    url = 'https://www.azlyrics.com/lyrics/' + band_name + '/' + song_name + '.html'

    try:
        response = requests.get(url)
        html_doc = response.text
        return html_doc
    except Exception as e:
        print("Error: ", e)
        return e

def extract_lyrics(html_doc):
    soup = BeautifulSoup(html_doc, 'html.parser')
    try:
        div = soup.find("div", {'class': 'ringtone'}).parent.find_all('div')[5]
        return div.get_text().strip()
    except Exception as e:
        print("Error while trying to parse text from HTML")
        raise e

def get_lyrics(band_name, song_name):
    html_doc = get_webpage(band_name, song_name)
    lyrics = extract_lyrics(html_doc)
    
    return lyrics
