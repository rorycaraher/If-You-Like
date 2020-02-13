import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# user = 
search_term = sys.argv[1]

client_credentials_manager = SpotifyClientCredentials(client_id='38ef923dcdc2419fb479849877c46c73', client_secret='05ce1147630843bcb1055f9cced752c5')

sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

results = sp.search(q=search_term,type='artist', limit=1)
# print(results['artists'])
resjson = json.dumps(results)
# print(resjson)
artist_id = results['artists']['items'][0]['id']

related_artists =  sp.artist_related_artists(artist_id)

for artist in related_artists['artists']:
    print(artist['name'])

# jsonrelartists = json.dumps(related_artists)

# print(jsonrelartists)