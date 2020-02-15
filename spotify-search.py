import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# user = 
search_term = sys.argv[1]

client_credentials_manager = SpotifyClientCredentials(client_id='38ef923dcdc2419fb479849877c46c73', client_secret='05ce1147630843bcb1055f9cced752c5')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q=search_term,type='album', limit=20)
json_results = json.dumps(results)
# albums = results['albums']['items']
# user_playlist_create(user, name, public=True, description='')
# print(json_results)

print("================ " + search_term + " ================")

for album in results['albums']['items']:
    print (album['name']+ ' - ' + album['uri'])

# print(json.dumps(albums))
