from pymongo import MongoClient

# client = MongoClient("mongodb+srv://cop4813:Khp24399@cluster0.zmr3h.mongodb.net/Cluster0?retryWrites=true&w=majority")
#
# db = client['db']
# print(db)
#
# expenses = db.expenses
# print(expenses)
#
# my_expenses = [{'description':'oranges', 'category':'groceries', 'cost':'10', 'date':'11/01/2020'},
#                {'description':'oranges', 'category':'groceries', 'cost':'10', 'date':'11/01/2020'}]
# result = expenses.insert_one(my_expenses[0])
# print(result)

client = MongoClient("mongodb+srv://cop4813:Khp24399@cluster0.zmr3h.mongodb.net/db?retryWrites=true&w=majority")
category_expenses = client.db.expenses.find({"category": "groceries"})
category_cost = 0
for i in category_expenses:
    category_cost += float(i["cost"])

print(category_cost)

