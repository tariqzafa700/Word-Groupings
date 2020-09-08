import time
from flask import Flask
from services.word_grouping_service import WordGroupingService

app = Flask(__name__)

service = WordGroupingService()

@app.route('/groupedWords/')
def group_init_words():
    return service.init_words(), 200


@app.route('/addWord/<word>', methods=['POST'])
def add_new_word(word: str):
    return service.add_word(word), 200
