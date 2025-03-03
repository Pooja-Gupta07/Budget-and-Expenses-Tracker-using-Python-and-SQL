def add_income(user_id, amount, source, date):
    sql = "INSERT INTO income (user_id, amount, source, date) VALUES (%s, %s, %s, %s)"
    values = (user_id, amount, source, date)
    cursor.execute(sql, values)
    conn.commit()
    print("Income added successfully!")

def add_expense(user_id, category, amount, description, date):
    sql = "INSERT INTO expenses (user_id, category, amount, description, date) VALUES (%s, %s, %s, %s, %s)"
    values = (user_id, category, amount, description, date)
    cursor.execute(sql, values)
    conn.commit()
    print("Expense added successfully!")
