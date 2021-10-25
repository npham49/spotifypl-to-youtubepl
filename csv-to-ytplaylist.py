#thanks to https://github.com/aditmodhvadia/SpotifyYouTubePlaylistManager/blob/master/create_playlist.py
import csv
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube"]

def read_csv(csv_filename):
    with open('playlists\\'+csv_filename+'.csv', mode='r') as inp:
        reader = csv.reader(inp)
        dict_from_csv = {rows[1]:rows[2] for rows in reader}
        del dict_from_csv['name']
    return dict_from_csv

def search_video(youtube,song_name):
    request = youtube.search().list(
        part="snippet",
        maxResults=25,
        q=song_name+" Music Video"
    )
    response = request.execute()
    for item in response['items']:
        print(item['snippet']['title'])
        print(item['id']['videoId'])
        return item['id']['videoId']

def create_new_youtube_playlist(youtube,playlist_title):
    #send a request forming a new playlist
    request = youtube.playlists().insert(
        part="snippet,status",
        body={
          "snippet": {
            "title": playlist_title,
            "description": "This is created from Spotify",
            "tags": [
              "Spotify",
              'API'
            ],
            "defaultLanguage": "en"
          },
          "status": {
            "privacyStatus": "private"
          }
        }
    )
    response = request.execute()

    return response
def insert_vid_to_pl(youtube,playlist_id:str,video_ids):
    for ids in video_ids:
        request = youtube.playlistItems().insert(
            part="snippet",
            body={
            "snippet": {
                "playlistId": playlist_id,
                "position": 0,
                "resourceId": {
                "kind": "youtube#video",
                "videoId": ids
                }
            }
            }
        )
        response = request.execute()
    print('enjoy!')

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    filename = input("Please input playlist name:")
    pl_dict = read_csv(filename)
    print(pl_dict)
    #List for all video ids
    video_ids = []
    for key in pl_dict.keys():
        video_ids.append(search_video(youtube,key+pl_dict[key]))

    #create youtube playlist
    yt_pl_title = input("What title would you like your playlist?")
    yt_playlist = create_new_youtube_playlist(youtube,yt_pl_title)
    insert_vid_to_pl(youtube,yt_playlist["id"],video_ids)




if __name__ == "__main__":
    main()