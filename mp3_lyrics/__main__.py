import id3_tools
from lyrics_fetchers import azlyrics
import os_tools
import sys

from progress.bar import Bar

if __name__ == '__main__':
    directory = sys.argv[1]
    mp3_files = os_tools.find_mp3_files(directory)

    bar = Bar('Progress', max=len(mp3_files))

    for mp3_file in mp3_files:
        bar.next()
        file_path = directory + mp3_file
        if id3_tools.is_lyrics_tag_present(file_path):
            # This file already has embedded lyrics. Skipping the file.
            continue

        band_name, song_name = id3_tools.get_song_details(file_path)

        try:
            lyrics = azlyrics.get_lyrics(band_name, song_name)
        except:
            # Error while downloading. Skipping this song.
            continue

        id3_tools.embed_lyrics(file_path, lyrics)
    
    bar.finish()
