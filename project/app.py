from flask import Flask, render_template
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Абсолютный путь к папке с app.py

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
    photos_folder = os.path.join(BASE_DIR, 'static', 'basic')  # Абсолютный путь к static/basic
    photo_files = os.listdir(photos_folder)
    return render_template('photos.html', photos=photo_files)

# Кнопка 2 - цветочки с подписями
@app.route('/flowers')
def flowers():
    flowers_folder = os.path.join(BASE_DIR, 'static', 'flowers')  # Абсолютный путь к static/flowers
    flower_files = os.listdir(flowers_folder)
    text_message = "your favorite bush roses and eustoma :) 💐"
    return render_template('flowers.html', flowers=flower_files, text_message=text_message)

# Кнопка 3 - песня с YouTube (новая ссылка)
@app.route('/song')
def song():
    youtube_url = "https://www.youtube.com/embed/0VAAS9xnS5U"
    return render_template('song.html', url=youtube_url)

# Кнопка 4 - текст из файла
@app.route('/text')
def text():
    text_file_path = os.path.join(BASE_DIR, 'formylove.txt')  # Абсолютный путь к файлу formylove.txt
    with open(text_file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return render_template('text.html', content=content)

# No Thanks экран
@app.route('/no')
def no():
    return render_template('no.html')

if __name__ == '__main__':
    app.run(debug=True)
