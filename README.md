# MP3-lyrics-embedder
Fetch lyrics from the internet and embed them into your MP3 files

## About
This uses ID3 tags in the mp3 files to get relevant information about the song for searching lyrics on one of the lyrics websites. The lyrics obtained is embedded as UnSynchronised Lyrics/Text (USLT) in the mp3 file. Supported media players will be able to display these lyrics when you play the song.

## Installation
1. Clone this repo.
2. Download [Mutagen](https://mutagen.readthedocs.io/en/latest/):
```
apt install python3-mutagen
```
3. Run mp3_lyrics.py with python3
```
python3 mp3_lyrics.py <directory-containing-mp3-files>
```
