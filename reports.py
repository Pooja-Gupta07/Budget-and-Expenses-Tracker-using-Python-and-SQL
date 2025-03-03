import matplotlib.pyplot as plt

def generate_report(user_id):
    sql = "SELECT category, SUM(amount) FROM expenses WHERE user_id = %s GROUP BY category"
    cursor.execute(sql, (user_id,))
    data = cursor.fetchall()

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.pie(amounts, labels=categories, autopct='%1.1f%%')
    plt.title("Expense Distribution")
    plt.show()
