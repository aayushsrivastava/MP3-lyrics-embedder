import id3_tools
from lyrics_fetchers import azlyrics
import os_tools
import sys

if __name__ == '__main__':
    directory = sys.argv[1]

    for mp3_file in os_tools.find_mp3_files(directory):
        file_path = directory + mp3_file
        if id3_tools.is_lyrics_tag_present(file_path):
            print("This file already has embedded lyrics. Skipping the file. (" + mp3_file + ")")
            continue

        band_name, song_name = id3_tools.get_song_details(file_path)

        try:
            print("[DOWNLOAD] " + band_name + " - " + song_name)
            lyrics = azlyrics.get_lyrics(band_name, song_name)
        except:
            print("Error while downloading. Skipping this song")
            continue

        print("[EMBED]    " + mp3_file)
        id3_tools.embed_lyrics(file_path, lyrics)