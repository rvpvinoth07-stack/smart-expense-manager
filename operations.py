from db import get_connection
from functools import reduce

# 1. Add User
def add_user(name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()
    print("User added successfully")


# 2. Add Expense
def add_expense(user_id, amount, category, description, date):
    conn = get_connection()
    cursor = conn.cursor()
    query = """INSERT INTO expenses (user_id, amount, category, description, date)
               VALUES (%s, %s, %s, %s, %s)"""
    cursor.execute(query, (user_id, amount, category, description, date))
    conn.commit()
    print("Expense added")


# 3. View Expenses (JOIN)
def view_expenses(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    SELECT u.name, e.amount, e.category, e.description, e.date
    FROM users u
    JOIN expenses e ON u.user_id = e.user_id
    WHERE u.user_id = %s
    """

    cursor.execute(query, (user_id,))
    data = cursor.fetchall()

    for row in data:
        print(row)

    return data


# 4. Filter Expenses
def filter_by_category(expenses, category):
    return list(filter(lambda x: x[2] == category, expenses))


def filter_by_date(expenses, date):
    return [exp for exp in expenses if exp[4] == date]


# 5. Total Expense (map + reduce)
def total_expense(expenses):
    amounts = list(map(lambda x: x[1], expenses))
    return reduce(lambda x, y: x + y, amounts, 0)


# 6. Category-wise Spending
def category_spending(expenses):
    return {
        cat: sum([e[1] for e in expenses if e[2] == cat])
        for cat in set(e[2] for e in expenses)
    }


# 7. Highest Expense
def highest_expense(expenses):
    return reduce(lambda x, y: x if x[1] > y[1] else y, expenses)


# 8. Monthly Report
def monthly_report(expenses):
    report = {}
    for e in expenses:
        month = str(e[4])[:7]   # YYYY-MM
        report[month] = report.get(month, 0) + e[1]
    return report


# 9. Smart Insight
def smart_insight(expenses):
    category_data = category_spending(expenses)
    highest = max(category_data, key=category_data.get)

    return f"You are spending too much on {highest}"