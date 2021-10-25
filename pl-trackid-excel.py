#Made thanks to https://morioh.com/p/31b8a607b2b0
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import time 
import os

#set environment variables
os.environ['SPOTIPY_CLIENT_ID'] = '' #enter your clientid and secret here from Spotify Developer
os.environ['SPOTIPY_CLIENT_SECRET']=''
#this is so we can use sp. commands
auth_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(auth_manager=auth_manager)

def getTrackID(user,playlist_id):
    #Input: username and playlist URI
    #Purpose: add every trackid into a list called ids
    #Output: 1st value:a list of trackid in a playlist
    #        2nd value: playlist's name in string 
    ids=[]
    playlist_name = 'PL-'
    playlist = sp.user_playlist(user,playlist_id)
    for item in playlist['tracks']['items']:
        track = item['track']
        ids.append(track['id'])
    for i in playlist['name']:
        if i==' ':
            break
        playlist_name += i

    return ids,playlist_name



def getTrackFeatures(id):
    meta=sp.track(id)


    #meta
    name = meta['name']
    artist = meta['album']['artists'][0]['name']

    track = [name,artist]
    return track




def main():
        #Promt user to input their username and playlist URI
    username = input("Please input your user name:")
    playlist_URI = input("Please input your playlist URI:")

    #create a list of ids in the playlist input
    ids,playlist_name = getTrackID(username, playlist_URI)

    #Debugging
    print(len(ids))
    print(ids)
    print(playlist_name)

    #loop over track ids 
    tracks = []
    for i in range(len(ids)):
        time.sleep(.005)
        track = getTrackFeatures(ids[i])
        tracks.append(track)

    # create dataset

    df = pd.DataFrame(tracks, columns = ['name', 'artist'])
    df.to_csv('playlists\\'+playlist_name+'.csv', sep = ',')

if __name__ == "__main__":
    main()