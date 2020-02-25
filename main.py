import os
from flask import Flask, render_template, request
from config import Config
from if_you_like import IfYouLike
from forms import ArtistSearchForm

app = Flask(__name__)
app.config.from_object(Config)
ifyoulike = IfYouLike()

@app.route('/')
def index():
    form = ArtistSearchForm()
    return render_template('index.html', form=form)
    
@app.route('/related-artists', methods=['GET', 'POST'])
def related_artists():
    form = ArtistSearchForm()
    search_term = request.form['search_term']
    results = ifyoulike.get_related_artists(search_term)
    return render_template('related-artists.html', searched_artist = results['searched_artist'], artist_id = results['artist_id'], artists = results['artists'], form = form)

@app.route('/artist-albums', methods=['GET', 'POST'])
def artist_albums():
    artist_id = request.args.get('artist_id')
    results = ifyoulike.get_artist_albums(artist_id)
    return render_template('artist-albums.html', albums = results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)