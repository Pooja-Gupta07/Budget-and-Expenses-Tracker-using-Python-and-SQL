def set_budget(user_id, category, limit_amount):
    sql = "INSERT INTO budget (user_id, category, limit_amount) VALUES (%s, %s, %s)"
    values = (user_id, category, limit_amount)
    cursor.execute(sql, values)
    conn.commit()
    print(f"Budget for {category} set to {limit_amount}")

def check_budget(user_id, category):
    sql = """SELECT SUM(amount) FROM expenses WHERE user_id = %s AND category = %s"""
    cursor.execute(sql, (user_id, category))
    total_expense = cursor.fetchone()[0] or 0

    sql = "SELECT limit_amount FROM budget WHERE user_id = %s AND category = %s"
    cursor.execute(sql, (user_id, category))
    budget_limit = cursor.fetchone()

    if budget_limit and total_expense > budget_limit[0]:
        print(f"Warning! You have exceeded your budget for {category}.")
