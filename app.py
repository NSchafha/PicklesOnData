from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


# Experiences
@app.route('/Experiences/coop_coop1.html')
def coop_coop1():
    return render_template('Experiences/coop_coop1.html')

@app.route('/Experiences/coop_coop2.html')
def coop_coop2():
    return render_template('Experiences/coop_coop2.html')

@app.route('/Experiences/coop_lao.html')
def coop_lao():
    return render_template('Experiences/coop_lao.html')


if __name__ == '__main__':
    app.run(debug=True)