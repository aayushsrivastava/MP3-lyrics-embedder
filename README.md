# MP3-lyrics-embedder
Fetch lyrics from the internet and embed them into your MP3 files

## About
This uses ID3 tags in the mp3 files to get relevant information about the song for searching lyrics on one of the lyrics websites. The lyrics obtained is embedded as UnSynchronised Lyrics/Text (USLT) in the mp3 file. Supported media players will be able to display these lyrics when you play the song.

## Installation
1. Install dependencies: [Mutagen](https://mutagen.readthedocs.io/en/latest/), [BeautifulSoup](https://pypi.org/project/beautifulsoup4/) and [Progress](https://pypi.org/project/progress/)
```
apt install python3-mutagen
pip install beautifulsoup4
pip install progress
```
2. Clone this repo
```
git clone https://github.com/aayushsrivastava/MP3-lyrics-embedder
cd MP3-lyrics-embedder
```
3. Run the program with python3
```
python3 mp3_lyrics <directory-containing-mp3-files>
```
