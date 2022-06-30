# Introduction
By manipulating the Spotify Python API and YouTube Big Data v3 this script converts a playlist from Spoitfy to Youtube

# How it works
The pl-trackid-excel.py script will create a request to Spotify server to extract your playlist's songs, the output it to a .csv file you named using Pandas.
The csv-to-ytplaylist.py script will then send a request to Youtube API to create a playlist with each song from the .csv file.

# Dependancies
- spotipy
- googleapiclient

# How to run
First grab your api client id and secret from Spotify Developer and then add it to the variable in pl-track-id.py, then grab your client_secret.json from Google Developers for YouTube Big Data v3, place the client_secret.json in the same spot as the .py files.
Second, grab your playlist's URI and run pl-trackid-excel.py, follow the input prompts.
Third, check the .csv file in playlists folder to make sure all the songs are correct.
Fouth, run csv-to-ytplaylist.py and follow the input prompts, you will be asked to log in to your Google account.
