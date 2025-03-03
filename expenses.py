def get_income(user_id):
    sql = "SELECT source, amount, date FROM income WHERE user_id = %s ORDER BY date DESC"
    cursor.execute(sql, (user_id,))
    return cursor.fetchall()

def get_expenses(user_id):
    sql = "SELECT category, amount, date FROM expenses WHERE user_id = %s ORDER BY date DESC"
    cursor.execute(sql, (user_id,))
    return cursor.fetchall()
