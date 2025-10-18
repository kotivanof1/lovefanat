from flask import Flask, render_template
import os

app = Flask(__name__)

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Экран подарка после Yes
@app.route('/gift')
def gift():
    return render_template('gift.html')

# Кнопка 1 - фотографии
@app.route('/photos')
def photos():
    photo_files = os.listdir('static/basic')  # Папка с фотографиями
    return render_template('photos.html', photos=photo_files)

# Кнопка 2 - цветочки с подписями
@app.route('/flowers')
def flowers():
    flower_files = os.listdir('static/flowers')  # Папка с картинками цветочков
    text_message = "your favorite bush roses and eustoma :) 💐"  # Здесь вставь текст, который хочешь показать
    return render_template('flowers.html', flowers=flower_files, text_message=text_message)

# Кнопка 3 - песня с YouTube (новая ссылка)
@app.route('/song')
def song():
    youtube_url = "https://www.youtube.com/embed/0VAAS9xnS5U"  # ссылка на новую песню
    return render_template('song.html', url=youtube_url)

# Кнопка 4 - текст из файла
@app.route('/text')
def text():
    with open('formylove.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template('text.html', content=content)

# No Thanks экран
@app.route('/no')
def no():
    return render_template('no.html')

if __name__ == '__main__':
    app.run(debug=True)
