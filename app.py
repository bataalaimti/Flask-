from flask import Flask, render_template, request
from Flask import game_rps, voice_word


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    нас = int("31")
    төгрөг = 0
    if request.method == 'POST':
        usd = request.form['name']
        төгрөг = int(usd)*2744
        # euro = round(game_rps.multiply_numbers(int(usd)),2)

    return render_template('index.html', name='Batdelger', нас=нас, дүн=төгрөг, ханш=2744)


@app.route('/voice', methods=['GET', 'POST'])
def voice():
    word = ""
    if request.method == 'POST':
        word = request.form['word']
        voice_word.txt_voice(word)
    return render_template('voice.html', result=word)


@ app.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')


@ app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/game', methods=['GET', 'POST'])
def game():
    game = ''
    if request.method == 'POST':
        user_guess = request.form['game']
        game = game_rps.game_rps(user_guess)
    return render_template('game.html', game_result=game)


if __name__ == '__main__':
    app.run()


# set FLASK_APP=app.py
# $env:FLASK_ENV='development'

