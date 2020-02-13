import sys
import json
import requests
from bs4 import BeautifulSoup
import am_best_album

search_term = sys.argv[1]
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
search_response = am_best_album.get_search_response(search_term)

print(search_response)