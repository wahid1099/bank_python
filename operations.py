import pymysql

conn = pymysql.connect(
    host="localhost",
    user="wahid",
    passwd="Wahid@#81",
    database="bank"
)


def create_account(name, balance):
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO accounts (name, balance) VALUES (%s, %s)", (name, balance))
    conn.commit()
    cursor.close()


def deposit(account_id, amount):
    cursor = conn.cursor()

    cursor.execute(
        "SELECT balance FROM accounts WHERE id = %s", (account_id))
    result_set = cursor.fetchone()
    if not result_set:
        print(f"Error: User with ID {account_id} not found in database")
    else:
        balance = result_set[0]
    # print(balance)
        new_balance = balance + amount
        cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s",
                       (new_balance, account_id))
        print("balance updated successfully!!")
        conn.commit()
        cursor.close()

# def withdraw(account_id, amount):
#     cursor = conn.cursor()
#     cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id))
#     balance = cursor.fetchone()[0]
#     if amount > balance:
#         raise ValueError("Insufficient balance")

#     new_balance = balance - amount
#     cursor.execute("UPDATE accounts SET balance = %s WHERE id = %s", (new_balance, account_id))
#     conn.commit()
#     cursor.close()

# def balance_check(account_id):
#     cursor = conn.cursor()
#     cursor.execute("SELECT balance FROM accounts WHERE id = %s", (account_id))
#     balance = cursor.fetchone()[0]
#     cursor.close()

#     return balance
