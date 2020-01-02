from flask import Flask, Response, jsonify, request
import requests
from parser import *

app = Flask(__name__)
movies = load_namelinks('movie_list.txt')
musics = load_namelinks('music_list.txt')
books = load_namelinks('book_list.txt')
raw_dict = {'movie': movies, 'music': musics, 'book': books}


@app.route('/')
def hello_world():
    return 'Resource Master'


@app.route('/resource', methods=['POST'])
def parse_resource():

    print(request.data)
    print(request.get_json())
    print(request.args)
    print(request.form)

    # Retrieve data
    _name = request.form.get('name')
    _type = request.form.get('type')
    _nums = int(request.form.get('nums', '10'))
    rand_idx = random_choice(len(raw_dict[_type]), _nums)

    base_dict = {
        'movie': {i: movies[i] for idx, i in enumerate(movies) if idx in rand_idx},
        'music': {i: musics[i] for idx, i in enumerate(musics) if idx in rand_idx},
        'book': {i: books[i] for idx, i in enumerate(books) if idx in rand_idx}
    }

    bases = base_dict[_type]
    urls = {i: bases[i] + _name for i in bases}

    if _type is None:
        urls = {}

    print(urls)
    return jsonify({'sitenames': list(urls.keys()), 'urls': list(urls.values())})


if __name__ == '__main__':
    app.run(debug=True)
