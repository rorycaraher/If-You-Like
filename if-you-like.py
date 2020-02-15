import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import secrets

class IfYouLike:
    def __init__(self):
        self.client_credentials_manager = SpotifyClientCredentials(secrets.client_id, secrets.client_secret)
        self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)

    def get_related_artists(self, search_term):
        results = self.sp.search(q=search_term,type='artist', limit=1)
        artist_id = results['artists']['items'][0]['id']
        return  self.sp.artist_related_artists(artist_id)

    def get_albums(self, search_term):
        artists = self.get_related_artists(search_term)['artists']
        albums = []
        for artist in artists:            
            results = self.sp.artist_albums(artist['uri'], album_type='album')
            albums.append(results['items'][0])
        return albums

    def create_playlist(self, search_term):
        playlist_title = 'If You Like ' + search_term
        self.sp.user_playlist_create(secrets.user_id, playlist_title, public=True)
        return 'playlist created!'

    def add_albums_to_playlist(self):
        pass

fugazi = IfYouLike()

print(fugazi.create_playlist('fugazi'))