from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Minha primeira aplicação flask na vercel!'

@app.route('/result')
def result():
   dict = {'phy':50,'che':60,'maths':70}
   return render_template('result.html', result = dict)
