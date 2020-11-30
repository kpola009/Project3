from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField

app = Flask(__name__)
app.config["SECRET_KEY"] = "Khp24399"
app.config["MONGO_URI"] = "mongodb+srv://cop4813:Khp24399@cluster0.zmr3h.mongodb.net/db?retryWrites=true&w=majority"
mongo = PyMongo(app)

class Expenses(FlaskForm):
    description = StringField("Description")
    category = SelectField("Category",
                           choices=[('rent', "rent"),
                                    ('electricity', "electricity"),
                                    ('water', "water"),
                                    ('insurance', "insurance"),
                                    ('restaurants', "restaurants"),
                                    ('groceries', "groceries"),
                                    ('gas', "gas"),
                                    ('college', "college"),
                                    ('party', "party"),
                                    ('mortgage', "mortgage")])
    cost = DecimalField("Cost")
    date = DateField("Date")

def get_total_expenses(category):

    category_cost = 0
    query = {"category": category}
    category_expenses = mongo.db.expenses.find(query)

    for i in category_expenses:
        category_cost += float(i["cost"])
    return category_cost

@app.route('/')
def index():
    my_expenses = mongo.db.expenses.find()
    total_cost = 0

    for i in my_expenses:
        total_cost += float(i["cost"])



    expensesByCategory = [
        ("rent", get_total_expenses("rent")),
        ("electricity", get_total_expenses("electricity")),
        ("water", get_total_expenses("water")),
        ("insurance", get_total_expenses("insurance")),
        ("restaurants", get_total_expenses("restaurants")),
        ("groceries", get_total_expenses("groceries")),
        ("gas", get_total_expenses("gas")),
        ("college", get_total_expenses("college")),
        ("party", get_total_expenses("party")),
        ("mortgage", get_total_expenses("mortgage")),
    ]

    return render_template("index.html", expenses=total_cost, expensesByCategory=expensesByCategory)


@app.route('/addExpenses', methods=["GET", "POST"])
def addExpenses():
    expensesForm = Expenses(request.form)
    if request.method == "POST":

        description_post = request.form["description"]
        category_post = request.form["category"]
        cost_post = request.form["cost"]
        date_post = request.form["date"]

        record = {'description': description_post, 'category': category_post, 'cost': float(cost_post), 'date': date_post}

        mongo.db.expenses.insert_one(record)

        return render_template("expenseAdded.html")
    return render_template("addExpenses.html", form=expensesForm)

app.run()