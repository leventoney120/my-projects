from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
    return render_template('index.html', number1 = 7000, number2 = 9000)

@app.route('/mult')
def number():
    var1, var2 = 3040, 7080
    return render_template('body.html', number1 = var1, number2 = var2, multiplication = var1*var2)

if __name__ == '__main__':
    app.run(debug=True)