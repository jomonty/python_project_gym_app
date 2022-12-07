from flask import render_template, request, redirect
from flask import Blueprint

from models.news import News

import repositories.news_repo as news_repo

homepage_blueprint = Blueprint('', __name__)

# READ - GET - SHOW TOP 3
@homepage_blueprint.route('/', methods=['GET'])
def homepage_news_top_3():
    news = news_repo.select_latest_x(3)
    return render_template('index.html', news=news, create=False, top_3=True)

# READ - GET - SHOW ALL
@homepage_blueprint.route('/all_news', methods=['GET'])
def homepage_news_all():
    news = news_repo.select_all()
    return render_template('index.html', news=news, create=False, top_3=False)

# CREATE - GET - SHOW TOP 3 & FORM
@homepage_blueprint.route('/new', methods=['GET'])
def homepage_news_new():
    news = news_repo.select_latest_x(3)
    return render_template('index.html', news=news, create=True, top_3=True)

# CREATE - POST - Process Request
@homepage_blueprint.route('/new', methods=['POST'])
def homepage_news_new_save():
    form_data = request.form
    new_news = News(form_data['news_item'])
    new_news = news_repo.save_one(new_news)
    return redirect('/')