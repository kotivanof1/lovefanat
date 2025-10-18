from flask import Flask, render_template
import os

# --- Початок змін для фіксації шляхів ---
# 1. Визначаємо абсолютний шлях до папки, в якій знаходиться app.py (тобто папка 'project')
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
# --- Кінець змін для фіксації шляхів ---

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
    # Используем абсолютный путь для доступа к папке static/basic
    photo_dir = os.path.join(BASE_DIR, 'static', 'basic') 
    
    # Добавляем обработку ошибок на случай, если папка все еще не найдена
    try:
        photo_files = os.listdir(photo_dir)  # Папка с фотографиями
    except FileNotFoundError as e:
        # Выводим ошибку в консоль и возвращаем сообщение
        print(f"Error: Directory not found at {photo_dir}. Original error: {e}")
        return "Ошибка: Папка static/basic не найдена на сервере.", 500
        
    return render_template('photos.html', photos=photo_files)

# Кнопка 2 - цветочки с подписями
@app.route('/flowers')
def flowers():
    # Используем абсолютный путь для доступа к папке static/flowers
    flower_dir = os.path.join(BASE_DIR, 'static', 'flowers')
    
    try:
        flower_files = os.listdir(flower_dir)  # Папка с картинками цветочков
    except FileNotFoundError as e:
        print(f"Error: Directory not found at {flower_dir}. Original error: {e}")
        return "Ошибка: Папка static/flowers не найдена на сервере.", 500
        
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
    # Используем абсолютный путь для доступа к файлу formylove.txt
    text_path = os.path.join(BASE_DIR, 'formylove.txt')
    
    try:
        with open(text_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError as e:
        print(f"Error: File not found at {text_path}. Original error: {e}")
        return "Ошибка: Файл formylove.txt не найден на сервере.", 500
        
    return render_template('text.html', content=content)

# No Thanks экран
@app.route('/no')
def no():
    return render_template('no.html')

if __name__ == '__main__':
    # Используем порт из окружения Render, если он доступен (для корректной работы на сервере)
    port = int(os.environ.get("PORT", 5000))  
    app.run(host="0.0.0.0", port=port, debug=True)  
