from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def menu():
    pizzas = [
        {"name": "Маргарита", "ingredients": "Сир, помідори, базилік", "price": "150 грн"},
        {"name": "Пепероні", "ingredients": "Сир, пепероні, соус", "price": "180 грн"},
        {"name": "Вегетаріанська", "ingredients": "Сир, овочі, соус", "price": "160 грн"}
    ]
    return render_template('menu.html', pizzas=pizzas)

if __name__ == '__main__':
    app.run(debug=True)
