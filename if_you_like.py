import sys
import json
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util
import secrets

class IfYouLike:
    def __init__(self):
        # self.client_credentials_manager = SpotifyClientCredentials(secrets.client_id, secrets.client_secret)
        # self.sp = spotipy.Spotify(client_credentials_manager=self.client_credentials_manager)
        scope = 'playlist-modify-public'
        self.token = util.prompt_for_user_token(secrets.username, scope, secrets.client_id, secrets.client_secret, 'https://example.com/callback/')
        self.sp = spotipy.Spotify(auth=self.token)

    def get_related_artists(self, search_term):
        results = self.sp.search(q=search_term,type='artist', limit=1)
        searched_artist = results['artists']['items'][0]['name']
        artist_id = results['artists']['items'][0]['id']
        return  {
            'searched_artist': searched_artist,
            'artist_id': artist_id,
            'artists': self.sp.artist_related_artists(artist_id)['artists']
        }

    def get_artist_albums(self, artist_id):
        results = self.sp.artist_albums(artist_id)
        albums = results['items']
        return albums

    # this will fail if artist only has EPs
    def get_album_tracks(self, search_term):
        artists = self.get_related_artists(search_term)['artists']
        tracks = []
        for artist in artists:            
            result = self.sp.artist_albums(artist['uri'], album_type='album')
            album = result['items'][0]
            album_tracks = self.sp.album_tracks(album['id'])
            print(json.dump(album_tracks))
            # for track in album_tracks:
            #     print(track)

        return tracks

    def create_playlist(self, search_term):
        tracks = self.get_album_tracks(search_term)
        track_ids = []
        for track in tracks:
            print(track['total'])
        #     track_ids.append(track['id'])
        # playlist_title = 'If You Like ' + search_term
        # playlist = self.sp.user_playlist_create(secrets.user_id, playlist_title, public=True)
        # add_tracks = self.sp.user_playlist_add_tracks(secrets.username, playlist['id'], track_ids)
        # return add_tracks
