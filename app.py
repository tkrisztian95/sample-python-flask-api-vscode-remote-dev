import requests
from bs4 import BeautifulSoup

from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route('/hello')
def hello():
    return "Hello World!"

from model.topMovie import TopMovie

@app.route("/imdb/movies/top250")
def get_imdb_top_movies():
    URL = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    data = []
    table = soup.find('table', attrs={'data-caller-name':'chart-top250movie'})
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) # Get rid of empty values

    movies=[]
    serialized=[]
    for row in rows:
        rank = row.find('td', attrs={'class':'titleColumn'}).text.splitlines()[1].strip()
        print(rank)

        title = row.find('td', attrs={'class':'titleColumn'}).find('a').text
        print(title)

        rating = row.find('td', attrs={'class':'ratingColumn imdbRating'}).find('strong').text
        print(rating)
        print("----------")

        movie = TopMovie(rank, title, rating)
        movies.append(movie)
        serialized.append(movie.serialize())        

    return jsonify(results=serialized)