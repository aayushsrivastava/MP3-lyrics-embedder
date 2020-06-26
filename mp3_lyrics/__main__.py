import id3_tools
from lyrics_fetchers import azlyrics
import os_tools

from argparse import ArgumentParser
from progress.bar import Bar

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="inputdir", required=True,
                    help="use audio files inside the directory DIR (Required)", metavar="DIR")
parser.add_argument("--website", dest="website", default="auto",
                    help="use specific website (azlyrics, genius, darklyrics)", metavar="WEBSITE")
parser.add_argument("--overwrite",
                    action="store_true", dest="overwrite", default=False,
                    help="operate on the input folder itself. The default behaviour is making a duplicate folder and leaving the original intact.")
parser.add_argument("-v", "--verbose",
                    action="store_true", dest="verbose", default=False,
                    help="print status messages to stdout")
parser.add_argument("-l", "--log", dest="logfile", 
                    help="write report to FILE", metavar="FILE")

args = parser.parse_args()

SHOW_PROGRESS      = not args.verbose
LOG_FILE           = args.logfile
OVERWRITE_ORIGINAL = args.overwrite
WEBSITE            = args.website
IN_DIRECTORY       = args.inputdir

if not IN_DIRECTORY.endswith("/"):
    IN_DIRECTORY = IN_DIRECTORY+"/"

if OVERWRITE_ORIGINAL:
    OUT_DIRECTORY = IN_DIRECTORY
else:
    OUT_DIRECTORY = IN_DIRECTORY[:-1] + " (copy)/"
    os_tools.copy_directory(IN_DIRECTORY, OUT_DIRECTORY)

# effectively the working directory from now on
directory = OUT_DIRECTORY
mp3_files = os_tools.find_mp3_files(directory)

if SHOW_PROGRESS:
    bar = Bar('Progress', max=len(mp3_files))

for mp3_file in mp3_files:
    if SHOW_PROGRESS:
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

if SHOW_PROGRESS:    
    bar.finish()
