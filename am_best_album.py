import sys
import json
import requests
from bs4 import BeautifulSoup

# ========================================================================
# get the argument
# set headers so the query doesn't get rejected!
# ========================================================================
search_term = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

# ========================================================================
# do a search
# ========================================================================
def get_search_response(search_term):
    search_url = 'https://www.allmusic.com/search/all/' + search_term
    return requests.get(search_url, headers=headers)
    
search_response = get_search_response(search_term)

# ========================================================================
# search results
# ========================================================================
def get_artist_id(search_response):
    search_results = BeautifulSoup(search_response.text, 'html.parser')
    first_artist = search_results.find('li', attrs={'class': 'artist'})
    artist_link = first_artist.find('a')
    tooltip = json.loads(artist_link.attrs['data-tooltip'])
    return tooltip['id']

artist_id = get_artist_id(search_response)

# ========================================================================
# discography page
# ========================================================================
def get_artist_and_picks(artist_id):
    discography_url = 'https://www.allmusic.com/artist/' + artist_id + '/discography'
    discography_response = requests.get(discography_url, headers=headers)
    discography_page = BeautifulSoup(discography_response.text, 'html.parser')
    artist = discography_page.title.text.split('|')[0].strip()
    picks = discography_page.findChildren('tr', attrs={"class": "pick"})
    return [artist, picks]

artist = get_artist_and_picks(artist_id)[0]
picks = get_artist_and_picks(artist_id)[1]


# ========================================================================
# output
# ========================================================================
# TODO: get release year also!
# TODO: display link to artist page also!
if picks:
    album_list = []
    for pick in picks:
        title_year = pick.findChildren('td', attrs={"class": "title"})[0].text.strip() + ' - ' + pick.findChildren('td', attrs={"class": "year"})[0].text.strip()
        album_list.append(title_year)

    print(artist + ', eh? You should start with: ')
    for album in album_list:
        print(album)
else:
    print('Not sure where to start with ' + artist + '...')
