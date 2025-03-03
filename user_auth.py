import hashlib

def register_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    values = (username, hashed_password)
    cursor.execute(sql, values)
    conn.commit()
    print("User registered successfully!")

def login_user(username, password):
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    sql = "SELECT user_id FROM users WHERE username = %s AND password = %s"
    cursor.execute(sql, (username, hashed_password))
    user = cursor.fetchone()
    return user[0] if user else None
