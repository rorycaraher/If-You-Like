import os
from flask import Flask, render_template, request
from if_you_like import IfYouLike

app = Flask(__name__)
ifyoulike = IfYouLike()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/related-artists')
def related_artists():
    results = ifyoulike.get_related_artists("grandaddy")
    return render_template('related-artists.html', results = results)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)