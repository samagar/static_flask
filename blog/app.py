from flask_frozen import Freezer
from flask import Flask, render_template, url_for
from flask_flatpages import FlatPages
from datetime import datetime

app = Flask(__name__)
app.config['FLATPAGES_EXTENSION'] = '.md'

pages = FlatPages(app)

@app.route('/<path:path>.html')
def page(path):
    page = pages.get_or_404(path)
    return render_template('page.html', page=page)

@app.route('/blog.html')
def index():
    posts = [p for p in pages if "date" in p.meta]
    sorted_pages=sorted(posts, reverse=True, key=lambda page:datetime.strptime(page.meta["date"], "%d %b %y"))
    
    return render_template('bloglist.html', pages=sorted_pages)

@app.route('/')
def home():
    return render_template('portfolio.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)