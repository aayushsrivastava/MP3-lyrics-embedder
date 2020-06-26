from mutagen.easyid3 import EasyID3
from mutagen.id3 import ID3NoHeaderError
from mutagen.id3 import ID3, USLT
from mutagen.id3 import Encoding

def embed_lyrics(file, lyrics):
    audio_file = ID3(file)

    if not is_lyrics_tag_present(file):
        audio_file[u'USLT'] = USLT(encoding=Encoding.UTF8, lang=u'eng', desc=u'', text=lyrics)
        audio_file.save(file)

def get_song_details(file):
    audio_file = EasyID3(file)
    band_name = audio_file['artist'][0]
    song_name = audio_file['title'][0]

    return band_name, song_name

def is_lyrics_tag_present(file):
    audio_file = ID3(file)
    return len(audio_file.getall(u"USLT")) > 0
